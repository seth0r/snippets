#!/usr/bin/env python3
'''
/*
 * Copyright (C) 2015  Sven Reißland
 * GFZ German Research Centre for Geosciences (http://www.gfz-potsdam.de)
 *
 * Licensed under the EUPL, Version 1.1 or - as soon they will be approved by
 * the European Commission - subsequent versions of the EUPL (the "Licence"),
 * complemented with the following provision: For the scientific transparency
 * and verification of results obtained and communicated to the public after
 * using a modified version of the work, You (as the recipient of the source
 * code and author of this modified version, used to produce the published
 * results in scientific communications) commit to make this modified source
 * code available in a repository that is easily and freely accessible for a
 * duration of five years after the communication of the obtained results.
 * 
 * You may not use this work except in compliance with the Licence.
 * 
 * You may obtain a copy of the Licence at:
 * https://joinup.ec.europa.eu/software/page/eupl
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the Licence is distributed on an "AS IS" basis,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the Licence for the specific language governing permissions and
 * limitations under the Licence.
 */
'''
import pymongo
import sys

if len(sys.argv)>3:
    f = open(sys.argv[1],"rt")
    dbe = pymongo.MongoClient()
    db = dbe[sys.argv[2]]
    coll = db[sys.argv[3]]
    cols = f.readline().strip().split(",")
    row = f.readline()
    while row!="":
        row = row.strip().split(",")
        e = {}
        for i in range(min(len(cols),len(row))):
            v = row[i]
            try:
                v = float(v)
                if v == int(v):
                    v = int(v)
            except:
                pass
            e[cols[i]] = v
        if len(e)>0:
            coll.insert(e)
        row = f.readline()
    f.close()
else:
    print("Usage: %s <csvfile> <mongodbdatabasename> <mongodbcollectionname>" % sys.argv[0])