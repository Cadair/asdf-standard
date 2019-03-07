import os
import asdf
from asdf import resolver as res

DIRNAME = os.path.dirname(__file__)

if DIRNAME == os.path.abspath(os.curdir):
    # Override the default ASDF url mapping so that all ASDF Standard schemas
    # resolve to the ones that are present in this repository, rather than
    # those that are installed with the ASDF python package. This allows for
    # much more direct testing of changes to schemas in this repository.
    ASDF_SCHEMA_URL_MAPPING = [
        (asdf.constants.STSCI_SCHEMA_URI_BASE,
         asdf.util.filepath_to_url(
            os.path.join(DIRNAME, 'schemas', 'stsci.edu'))
            + '/{url_suffix}.yaml')
    ]
    res.default_url_mapping = res.Resolver(ASDF_SCHEMA_URL_MAPPING, 'url')

    # Only add this plugin definition when not being run as part of a submodule
    pytest_plugins = [
        'asdf.tests.schema_tester'
    ]
