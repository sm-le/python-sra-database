# SRA metadata format
# contributors: smlee

# History
# 2024-04-07 v1.0.0 - first commit

# Module
from dataclasses import dataclass
from typing import List, Dict

# Main
@dataclass
class Submission(object):
    """SRA Submission class object
    
    Args:
        _data: dictionary fomatted row information
    """
    _data:Dict

    def __post_init__(self):
        """Post initialization
        """
        # Accessions
        self.studies:List = list()
        self.experiments:List = list()
        self.samples:List = list()
        self.runs:List = list()
        # Status and self accession
        self.accession:str = self._data.get('accession', None)
        self.status:str = self._data.get('status', None)
        self.updated:str = self._data.get('updated', None)
        self.published:str = self._data.get('published', None)
        self.received:str = self._data.get('received', None)
        self.center:str = self._data.get('center', None)
        self.visibility:str = self._data.get('visibility', None)
        self.replacedby:str = self._data.get('replacedby', None)

@dataclass
class Sample(object):
    """SRA Sample class object
    
    Args:
        _data: dictionary fomatted row information
    """
    _data:Dict

    def __post_init__(self):
        """Post initialization
        """
        # Sample and project
        self.accession:str = self._data.get('accession', None)
        self.submission:str = self._data.get('submission', None)
        self.biosample:str = self._data.get('biosample', None)
        self.updated:str = self._data.get('updated', None)
        self.published:str = self._data.get('published', None)
        self.received:str = self._data.get('received', None)

        # organism data
        self.taxid:int = None
        self.organism:str = None

@dataclass
class Run(object):
    """SRA Run class object
    
    Args:
        _data: dictionary fomatted row information
    """
    _data:Dict

    def __post_init__(self):
        """Post initialization
        """
        # Accession
        self.accession:str = self._data.get('accession', None)
        self.submission:str = self._data.get('submission', None)
        self.experiment:str = self._data.get('experiment', None)
        self.sample:str = self._data.get('sample', None)
        self.study:str = self._data.get('study', None)
        self.bioproject:str = self._data.get('bio_project', None)
        self.biosample:str = self._data.get('biosample', None)
        self.updated:str = self._data.get('updated', None)
        self.published:str = self._data.get('published', None)
        self.received:str = self._data.get('received', None)

@dataclass
class Study(object):
    """SRA Study class object

    Args:
        _data: dictionary fomatted row information
    """
    _data:Dict

    def __post_init__(self):
        """Post initialization
        """
        # Accession
        self.accession:str = self._data.get('accession', None)
        self.submission:str = self._data.get('submission', None)
        self.bioproject:str = self._data.get('bioproject', None)
        self.title:str = self._data.get('title', None)
        self.type:str = self._data.get('type', None)
        self.study_links:List = list()
        self.updated:str = self._data.get('updated', None)
        self.published:str = self._data.get('published', None)
        self.received:str = self._data.get('received', None)

@dataclass
class Experiment(object):
    """SRA Experiment class object

    Args:
        _data: dictionary fomatted row information
    """
    _data:Dict

    instrument:str = None
    strategy:str = None
    source:str = None
    selection:str = None
    layout:str = None
    def __post_init__(self):
        """Post initialization
        """
        self.accession:str = self._data.get('accession', None)
        self.submission:str = self._data.get('submission', None)
        self.bioproject:str = self._data.get('bioproject', None)
        self.biosample:str = self._data.get('biosample', None)
        self.updated:str = self._data.get('updated', None)
        self.published:str = self._data.get('published', None)
        self.received:str = self._data.get('received', None)