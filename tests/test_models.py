from datetime import datetime

import pytest
from pydantic import ValidationError

from vinea.models import Block, HourlyWeather


def test_kalokairini_ora_xoris_broxi_kai_anemo_ginetai_dekti():
    w = HourlyWeather(
        block_id="D1",
        timestamp=datetime(2026, 7, 15, 14, 0),
        temp_C=34.0,
        rel_humid=28.0,
        air_speed=0.0,
        rain=0.0,
    )
    assert w.rain == 0.0


def test_arnitiko_embado_aporriptetai():
    with pytest.raises(ValidationError):
        Block(
            id="D2",
            location="Δαφνές",
            variety="Βηλάνα",
            area_stremmata=-5,
            soil_type="αργιλώδες",
            root_depth_cm=90,
            irrigation_type="στάγδην",
        )
