#
# Module: Notes REST Controller
# 
# This controller handles REST calls 
# via Flask
# 
# 2013, Frank Caron

#Imports
from pythonotes import pythonotes
from pythonotes import DBHelper
import json
from flask import abort, jsonify

temp_helper = DBHelper.DBReader()

@pythonotes.route('/')
@pythonotes.route('/index')
def index():
    return "Frank's humble python web service beginnings, now with notes."

# REST Handlers
# -------------------
# Notes - GET
# Return collection of notes
@pythonotes.route('/notes/', methods = ['GET'])
def get_all_notes(): 
    temp = temp_helper.db_read_all()
    return jsonify( { 'notes': temp } )

# Note - GET
# Return a specified notes resource
@pythonotes.route('/notes/<int:note_id>', methods = ['GET'])
def get_specific_note(note_id): 
    temp = temp_helper.db_read_specific(note_id)
    if len(temp) == 0:
        abort(404) 
    return jsonify( { 'notes': temp } )
    
# Notepad - Get
# Returns all the notes associated with a specific notepad    
@pythonotes.route('/notepad/<int:notepad_id>', methods = ['GET'])
def get_specific_notepad(notepad_id): 
    temp = temp_helper.db_read_specific_notepad(notepad_id)
    if len(temp) == 0:
        abort(404) 
    return jsonify( { 'notes': temp } )
    
# Last Note Created - GET
# Returns the row ID for the last row created
@pythonotes.route('/notes/lastid', methods = ['GET'])
def get_last_note_id():
    return jsonify( { 'notes': temp_helper.db_get_last_row_id() } )