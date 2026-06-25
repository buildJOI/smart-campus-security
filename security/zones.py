ZONE_X1 = 100
ZONE_Y1 = 100

ZONE_X2 = 500
ZONE_Y2 = 400


def inside_zone(cx, cy):

    return (
        ZONE_X1 <= cx <= ZONE_X2 and
        ZONE_Y1 <= cy <= ZONE_Y2
    )