from hypothesis import strategies as st

import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_frontend_test


@handle_frontend_test(
    fn_tree="torch.bartlett_window",
    window_length=helpers.ints(min_value=2, max_value=100),
    periodic=st.booleans(),
    dtype=helpers.get_dtypes("float", full=False),
)
def test_torch_bartlett_window(
    window_length,
    periodic,
    dtype,
    on_device,
    fn_tree,
    frontend,
    test_flags,
    backend_fw,
):
    helpers.test_frontend_function(
        input_dtypes=[],
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        window_length=window_length,
        periodic=periodic,
        dtype=dtype[0],
        rtol=1e-02,
        atol=1e-02,
    )
