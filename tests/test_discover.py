"""scripts/discover_config.py: descubre la configuracion JSON de un processor a partir de lo que dice el servidor."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, ROOT)
import discover_config as dc  # noqa: E402


def test_set_path_builds_nested_dicts_from_an_attribute_path():
    cfg = {}
    dc.set_path(cfg, "/substringConfiguration/start", 1)
    dc.set_path(cfg, "/type", "SUBSTRING")
    dc.set_path(cfg, "/substringConfiguration/columnsToProcess", ["ciudad"])
    assert cfg == {"substringConfiguration": {"start": 1, "columnsToProcess": ["ciudad"]}, "type": "SUBSTRING"}


def test_guess_value_by_field_name():
    assert dc.guess_value("columnsToProcess") == ["ciudad"]
    assert dc.guess_value("newColumnName") == ""
    assert dc.guess_value("shouldCreateNewColumn") is False
    assert dc.guess_value("substringConfiguration") == {}  # un objeto de configuracion
    assert dc.guess_value("length") == 1 and dc.guess_value("startIndex") == 1
    assert dc.guess_value("pattern") == "x"


def test_enum_field_and_first_value_are_read_from_a_jackson_error():
    msg = ('"detail": "Cannot deserialize value of type `com.q.PadDirection` from String \\"zzz\\": not one of the values accepted '
           'for Enum class: [LEFT, RIGHT, BOTH]\\n at [Source: REDACTED] (through reference chain: com.q.WrappedDataflow'
           '[\\"graph\\"]->com.q.Graph[\\"nodes\\"]->java.util.ArrayList[2]->com.q.Node$Processor[\\"component\\"]->'
           'com.q.Strings[\\"paddingConfiguration\\"]->com.q.Padding[\\"direction\\"])"')
    assert dc.enum_field(msg) == ("paddingConfiguration", "direction", ["LEFT", "RIGHT", "BOTH"])
    assert dc.enum_field("sin enum") is None


def test_config_key_is_the_subtype_in_camel_case_plus_configuration():
    # los nombres reales de emulator/dfw.py TYPED
    assert dc.config_key("LOWERCASE") == "lowercaseConfiguration"
    assert dc.config_key("REMOVE_NON_NUM_CHARS") == "removeNonNumCharsConfiguration"
    assert dc.config_key("CONVERT_TO_NUMBER") == "convertToNumberConfiguration"
    assert dc.config_key("SPLIT_TEXT_IN_PARTS") == "splitTextInPartsConfiguration"
