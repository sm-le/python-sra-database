# Extract targeted text from a SRA file
# contibutors: smlee

# History
# 2024-04-07 v1.0.0 - first commit

# Module
from conf.path import sra_base

# Main
class SRATargetText(object):
    """SRA target text extractor
    """

    @classmethod
    def extract_target_text(cls,
                            *,
                            sra_submission:str,
                            target_accession:str,
                            target_type:str) -> str:
        """Extract lines of target text from a SRA file

        Args:
            sra_submission: SRA submission id
            target_accession: SRA target id
            target_type: SRA type of the target
        Returns:
            str(target text)
        """

        # logic switch to parse
        parse_b = False
        # result
        txt = """"""
        txt += '<?xml version="1.0" encoding="UTF-8"?>\n'
        txt += f'<{target_type.upper()}_SET xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
        
        # loop
        with open(f"{sra_base}/{sra_submission}/{sra_submission}.{target_type}.xml") as f:
            for line in f:
                if f'accession="{target_accession}"' in line:
                    parse_b = True
                if parse_b:
                    txt += line
                if parse_b and line.strip() == f'</{target_type.upper()}>':
                    break
        # filling last line
        txt += f'</{target_type.upper()}_SET>'
        
        return txt