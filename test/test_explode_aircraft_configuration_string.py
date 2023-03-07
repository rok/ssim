from ssim import ssim


def test_explode_aircraft_configuration_string(aircraft_configuration_strings):
    for aircraft_configuration_string in aircraft_configuration_strings:
        assert (
            ssim._explode_aircraft_configuration_string(
                aircraft_configuration_string["string"]
            )
            == aircraft_configuration_string["aircraft_configuration"]
        )
