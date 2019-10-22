import re

WELLBORE_REGEX = r"(\d{1,4})\/(\d{1,2})(-\w{1,2})*-(\d{1,2})( \w{1,2})*"


def parse_wellbore_name(txt):
    """Parse wellbore name
        Args:
            txt: str with wellbore name
        Returns:
            wellbores: dict with parsed wellbore name properties
                keys: quadrant, block, wellbore_id, well_number, well_type
    """
    mo = re.match(WELLBORE_REGEX, txt)
    if mo:
        quadrant, block, wellbore_id, well_number, well_type = mo.groups()
        if quadrant:
            quadrant = int(quadrant)
        if block:
            block = int(block)
        if wellbore_id:
            wellbore_id = wellbore_id[1:]
        if well_number:
            well_number = int(well_number)
        if well_type:
            well_type = well_type[1:]
        return f"{quadrant}/{block}-{well_number}"
    else:
        return None
