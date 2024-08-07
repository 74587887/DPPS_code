from abc import ABC, abstractmethod
import torch

__CONDITIONING_METHOD__ = {}


def register_conditioning_method(name: str):
    def wrapper(cls):
        if __CONDITIONING_METHOD__.get(name, None):
            raise NameError(f"Name {name} is already registered!")
        __CONDITIONING_METHOD__[name] = cls
        return cls

    return wrapper


def get_conditioning_method(name: str, operator, noiser, **kwargs):
    if __CONDITIONING_METHOD__.get(name, None) is None:
        raise NameError(f"Name {name} is not defined!")
    return __CONDITIONING_METHOD__[name](operator=operator, noiser=noiser, **kwargs)


class ConditioningMethod(ABC):
    def __init__(self, operator, noiser, **kwargs):
        self.operator = operator
        self.noiser = noiser

    def project(self, data, noisy_measurement, **kwargs):
        return self.operator.project(data=data, measurement=noisy_measurement, **kwargs)

    def grad_and_value(self, x_prev, x_0_hat, measurement, **kwargs):
        if self.noiser.__name__ == 'gaussian':
            difference = measurement - self.operator.forward(x_0_hat, **kwargs)
            norm = torch.linalg.norm(difference)
            norm_grad = torch.autograd.grad(outputs=norm, inputs=x_prev)[0]

        elif self.noiser.__name__ == 'poisson':
            Ax = self.operator.forward(x_0_hat, **kwargs)
            difference = measurement - Ax
            norm = torch.linalg.norm(difference) / measurement.abs()
            norm = norm.mean()
            norm_grad = torch.autograd.grad(outputs=norm, inputs=x_prev)[0]

        else:
            raise NotImplementedError

        return norm_grad, norm

    @abstractmethod
    def conditioning(self, x_t, measurement, noisy_measurement=None, **kwargs):
        pass


@register_conditioning_method(name='vanilla')
class Identity(ConditioningMethod):
    # just pass the input without conditioning
    def conditioning(self, x_t):
        return x_t


@register_conditioning_method(name='dpps')
class PosteriorSampling(ConditioningMethod):
    def __init__(self, operator, noiser, **kwargs):
        super().__init__(operator, noiser)
        self.scale = kwargs.get('scale', 1.0)

    def conditioning(self, x_prev, x_t, x_0_hat, measurement, pred_noise, frequency, idx, **kwargs):
        norm_grad, norm = self.grad_and_value(x_prev=x_prev, x_0_hat=x_0_hat, measurement=measurement, **kwargs)
        x_t = x_t - norm_grad * self.scale

        # creating n samples and choose the best one
        # number_of_sample = 20
        n_noise = torch.randn(frequency, *x_t.shape[1:], device=x_t.device)
        x_t_samples = x_t + torch.exp(0.5 * kwargs.get('log_variance')) * n_noise

        # expecting the sample point on the desired solution:
        # we find that using the pred_noise (epsilon) works better
        x_t_samples_minus_noise = (x_t_samples - kwargs.get('sqrt_one_minus_alphas_cumprod_prev')
                                   * pred_noise)  # which will go through operator
        differences = (kwargs.get('sqrt_alphas_cumprod_prev') * measurement -
                       self.operator.forward(x_t_samples_minus_noise, **kwargs))

        diff_norms = torch.linalg.norm(differences.reshape(frequency, -1), dim=1)
        best_idx = torch.argmin(diff_norms)
        best_noise = n_noise[best_idx]

        if idx != 0:
            x_t = x_t + torch.exp(0.5 * kwargs.get('log_variance')) * best_noise

        return x_t, norm
