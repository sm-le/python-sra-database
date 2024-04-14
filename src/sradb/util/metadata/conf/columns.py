# columns for meta data tables
# contributor: smlee

submission_c = [ "_id",
                 "study_accessions",
                 "experiment_accessions",
                 "sample_accessions",
                 "run_accessions",
                 "status",
                 "updated",
                 "published",
                 "received",
                 "center",
                 "visibility",
                 "replacedby" ]

sample_c = [ "_id",
             "submission_accession",
             "taxid",
             "organism_name",
             "biosample",
             "updated",
             "published",
             "received" ]

run_c = [ "_id",
          "submission_accession",
          "experiment_accession",
          "sample_accession",
          "study_accession",
          "bioproject",
          "biosample",
          "updated",
          "published",
          "received" ]

study_c = [ "_id",
            "submission_accession",
            "bioproject",
            "study_title",
            "study_type",
            "study_links",
            "updated",
            "published",
            "received" ]

experiment_c = [ "_id",
                 "submission_accession",
                 "bioproject",
                 "biosample",
                 "instrument",
                 "strategy",
                 "source",
                 "selection",
                 "layout",
                 "updated",
                 "published",
                 "received" ]