from ssim import ssim


def test_expand_slot(expanding_slots):
    for slot in expanding_slots:
        assert ssim._expand(slot["slot"]) == slot["flights"]
