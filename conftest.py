def pytest_addoption(parser):
    parser.addoption("--fn", action="store", default="default fn")
    parser.addoption("--station_fn", action="store", default="default station_fn")

def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.fn
    if 'fn' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("fn", [option_value])
    
    option_value = metafunc.config.option.station_fn
    if 'station_fn' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("station_fn", [option_value])