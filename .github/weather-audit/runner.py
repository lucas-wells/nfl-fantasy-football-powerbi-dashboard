import importlib.util
from pathlib import Path

p = Path(__file__).with_name('audit.py')
spec = importlib.util.spec_from_file_location('deadeye_audit', p)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

# nflverse schedule naming aliases that the fallback geocoder did not resolve.
audit.PATCH_NORM.update({
    audit.norm_stadium('Ring Central Coliseum'): (37.751667, -122.200556),
    audit.norm_stadium('TIAA Bank Stadium'): (30.323889, -81.6375),
})

audit.main()
