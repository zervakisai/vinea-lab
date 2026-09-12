from vinea.irrigation import needs_irrigation

def test_ksiro_xorafi_thelei_potisma():
	assert needs_irrigation(0.12, 0.15) is True
def test_yggro_xorafi_den_thelei():
	assert needs_irrigation(0.20,0.15) is False


