from ssim import ssim


def test_expand_slot(expanding_slots):
    for slot in expanding_slots:
        assert ssim._expand(slot["slot"]) == slot["flights"]


def test_roundtrip_slots(expanding_slots):
    for slot in expanding_slots:
        flights = ssim.expand_slots([slot["slot"]])

        assert slot["flights"] == flights
        assert slot["slot"] == ssim.compress_flights(flights)[0]
