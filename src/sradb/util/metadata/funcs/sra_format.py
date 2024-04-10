# SRA metadata format
# contributors: smlee

# History
# 2024-04-10 v1.0.1 - add get row method to all classes
# 2024-04-07 v1.0.0 - first commit

# Module
from dataclasses import dataclass
from typing import List, Dict
from ..conf.columns import *

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
    
    def get_row(self):
        """Get row information
        """
        hdr = submission_c
        row = [self.accession, 
               self.studies, 
               self.experiments, 
               self.samples, 
               self.runs, 
               self.status, 
               self.updated, 
               self.published, 
               self.received, 
               self.center, 
               self.visibility, 
               self.replacedby]
        
        return dict(zip(hdr, row))

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

    def get_row(self):
        """Get row information
        """
        hdr = sample_c
        row = [self.accession,
               self.submission,
               self.taxid,
               self.organism,
               self.biosample,
               self.updated,
               self.published,
               self.received]
        
        return dict(zip(hdr, row))

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
    
    def get_row(self):
        """Get row information
        """
        hdr = run_c
        row = [self.accession,
               self.submission,
               self.experiment,
               self.sample,
               self.study,
               self.bioproject,
               self.biosample,
               self.updated,
               self.published,
               self.received]
        
        return dict(zip(hdr, row))

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

    def get_row(self):
        """Get row information
        """
        hdr = study_c
        row = [self.accession,
               self.submission,
               self.bioproject,
               self.title,
               self.type,
               self.study_links,
               self.updated,
               self.published,
               self.received]
        
        return dict(zip(hdr, row))

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
    
    def get_row(self):
        """Get row information
        """
        hdr = experiment_c
        row = [self.accession,
               self.submission,
               self.bioproject,
               self.biosample,
               self.instrument,
               self.strategy,
               self.source,
               self.selection,
               self.layout,
               self.updated,
               self.published,
               self.received]
        
        return dict(zip(hdr, row))