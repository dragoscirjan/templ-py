
VERSION = (0, 1, 0, 'alpha', 0)

def get_version(version=VERSION):
    from cement.utils.version import get_version as cement_get_version
    return cement_get_version(version)

def get_static_version(version=VERSION):
    """Returns a PEP 386-compliant version number from VERSION."""
    assert len(version) == 5
    assert version[3] in ('alpha', 'beta', 'rc', 'final')

    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|c}N - for alpha, beta and rc releases

    parts = 2 if version[2] == 0 else 3
    main = '.'.join(str(x) for x in version[:parts])

    sub = ''
    if version[3] == 'alpha' and version[4] == 0:
            sub = 'a%d' % (version[4])

    elif version[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        sub = mapping[version[3]] + str(version[4])

    return main + sub
