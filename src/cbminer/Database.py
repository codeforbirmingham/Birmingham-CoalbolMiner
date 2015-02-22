'''
The MIT License (MIT)

Copyright (c) 2015 @ CodeForBirmingham (http://codeforbirmingham.org)
@Author: Marcus Dillavou <marcus.dillavou@codeforbirmingham.org>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

'''
This is a simple class to hold our
basic database information
'''

import sqlalchemy
import sqlalchemy.orm

from ConfigManager import ConfigManager

class Database(object):
    def __init__(self):
        cm = ConfigManager.get_instance()
        
        if not cm or cm.dbstring is None:
            raise Exception("Please configure the database first in the cbminer.ini")
        
        # This is a test, this should
        #  come from a configuration
        #self.engine = sqlalchemy.create_engine('sqlite:///:memory:', echo = True)
        #self.engine = sqlalchemy.create_engine('sqlite:///test.sqlite3')
        self.engine = sqlalchemy.create_engine(cm.dbstring)

        SessionKlass = sqlalchemy.orm.sessionmaker(bind = self.engine)
        self.session = SessionKlass()
