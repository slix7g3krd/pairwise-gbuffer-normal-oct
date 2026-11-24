import pytest
import graphics.gbuffer_normal_oct as mod

CASES = [
    ("oct_encode_sign", (1,)),
    ("mrt_channel_map", (1,)),
    ("same_frame_upsample", (1,)),
    ("depth_fence", (1,)),
    ("clear_on_camera", (1,)),
    ("normalize_check", (1,)),
    ("encode", (1,)),
    ("decode", (1,)),
    ("write_gbuffer", (1,)),
    ("lighting_pass", (1,)),
    ("validate_normals", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
