class ConverterABC(object):
    '''
    Simple class wrapper for parsing ABC.
    '''

    def __init__(self):
        # always create a score instance
        self._stream = stream.Score()

    def parseData(self, strData, number=None):
        '''
        Get ABC data, as token list, from a string representation.
        If more than one work is defined in the ABC data, a
        :class:`~music21.stream.Opus` object will be returned;
        otherwise, a :class:`~music21.stream.Score` is returned.
        '''
        af = abc.ABCFile()
        # do not need to call open or close
        abcHandler = af.readstr(strData, number=number)
        # set to stream
        if abcHandler.definesReferenceNumbers():
            # this creates an Opus object, not a Score object
            self._stream = abc.translate.abcToStreamOpus(abcHandler,
                number=number)
        else: # just one work
            abc.translate.abcToStreamScore(abcHandler, self._stream)

    def parseFile(self, fp, number=None):
        '''Get MIDI data from a file path. If more than one work is defined in the ABC data, a  :class:`~music21.stream.Opus` object will be returned; otherwise, a :class:`~music21.stream.Score` is returned.

        If `number` is provided, and this ABC file defines multiple works with a X: tag, just the specified work will be returned.
        '''
        #environLocal.printDebug(['ConverterABC.parseFile: got number', number])

        af = abc.ABCFile()
        af.open(fp)
        # returns a handler instance of parse tokens
        abcHandler = af.read(number=number)
        af.close()

        # only create opus if multiple ref numbers
        # are defined; if a number is given an opus will no be created
        if abcHandler.definesReferenceNumbers():
            # this creates a Score or Opus object, depending on if a number
            # is given
            self._stream = abc.translate.abcToStreamOpus(abcHandler,
                           number=number)
        # just get a single work
        else:
            abc.translate.abcToStreamScore(abcHandler, self._stream)

    def _getStream(self):
        return self._stream

    stream = property(_getStream)
