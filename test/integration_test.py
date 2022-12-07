from src.use_case import reverse_use_case


def test_valid_reverse_use_case():
    ret = reverse_use_case('example')
    assert 'result' in ret
    assert ret['result'] == 'elpmaxe'
