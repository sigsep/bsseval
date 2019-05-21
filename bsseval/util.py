import numpy as np


def pad_or_truncate(
    audio_reference,
    audio_estimates
):
    """Pad or truncate estimates by duration of references:
    - If reference > estimates: add zeros at the and of the estimated signal
    - If estimates > references: truncate estimates to duration of references

    Parameters
    ----------
    references : np.ndarray, shape=(nsrc, nsampl, nchan)
        array containing true reference sources
    estimates : np.ndarray, shape=(nsrc, nsampl, nchan)
        array containing estimated sources
    Returns
    -------
    references : np.ndarray, shape=(nsrc, nsampl, nchan)
        array containing true reference sources
    estimates : np.ndarray, shape=(nsrc, nsampl, nchan)
        array containing estimated sources
    """
    est_shape = audio_estimates.shape
    ref_shape = audio_reference.shape
    if est_shape[1] != ref_shape[1]:
        if est_shape[1] >= ref_shape[1]:
            audio_estimates = audio_estimates[:, :ref_shape[1], :]
        else:
            # pad end with zeros
            audio_estimates = np.pad(
                audio_estimates,
                [
                    (0, 0),
                    (0, ref_shape[1] - est_shape[1]),
                    (0, 0)
                ],
                mode='constant'
            )

    return audio_reference, audio_estimates