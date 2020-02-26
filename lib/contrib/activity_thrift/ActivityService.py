#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from __future__ import absolute_import
import six
from thrift.util.Recursive import fix_spec
from thrift.Thrift import *
from thrift.protocol.TProtocol import TProtocolException


import baseplate.thrift.BaseplateService
from .ttypes import *
from thrift.Thrift import TProcessor
import pprint
import warnings
from thrift import Thrift
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
from thrift.protocol import THeaderProtocol
try:
  from thrift.protocol import fastbinary
  if fastbinary.version < 2:
    fastbinary = None
    warnings.warn("Disabling fastbinary, need at least version 2")
except:
  fastbinary = None
try:
  from thrift.protocol import fastproto
except:
  fastproto = None

all_structs = []
UTF8STRINGS = bool(1) or sys.version_info.major >= 3
from thrift.util.Decorators import *

class Iface(baseplate.thrift.BaseplateService.Iface):
  def record_activity(self, context_id=None, visitor_id=None):
    """
    Register a visitor's activity within a given context.
    
    The visitor's activity will be recorded but will expire over time. If the
    user continues to be active within the context, this endpoint should be
    called occasionally to ensure they continue to be counted.
    
    This method is `oneway`; no indication of success or failure is returned.
    
    
    Parameters:
     - context_id
     - visitor_id
    """
    pass

  def count_activity(self, context_id=None):
    """
    Count how many visitors are currently active in a given context.
    
    The results of this call are cached for a period of time to ensure that if
    the count is fuzzed, the fuzzing is stable. This prevents repeated requests
    from revealing the range of fuzzing and therefore the true value.
    
    
    Parameters:
     - context_id
    """
    pass

  def count_activity_multi(self, context_ids=None):
    """
    Count how many visitors are active in a number of given contexts.
    
    This is the same as `count_activity` but allows for querying in batch.
    
    
    Parameters:
     - context_ids
    """
    pass


class ContextIface(baseplate.thrift.BaseplateService.ContextIface):
  def record_activity(self, handler_ctx, context_id=None, visitor_id=None):
    """
    Register a visitor's activity within a given context.
    
    The visitor's activity will be recorded but will expire over time. If the
    user continues to be active within the context, this endpoint should be
    called occasionally to ensure they continue to be counted.
    
    This method is `oneway`; no indication of success or failure is returned.
    
    
    Parameters:
     - context_id
     - visitor_id
    """
    pass

  def count_activity(self, handler_ctx, context_id=None):
    """
    Count how many visitors are currently active in a given context.
    
    The results of this call are cached for a period of time to ensure that if
    the count is fuzzed, the fuzzing is stable. This prevents repeated requests
    from revealing the range of fuzzing and therefore the true value.
    
    
    Parameters:
     - context_id
    """
    pass

  def count_activity_multi(self, handler_ctx, context_ids=None):
    """
    Count how many visitors are active in a number of given contexts.
    
    This is the same as `count_activity` but allows for querying in batch.
    
    
    Parameters:
     - context_ids
    """
    pass


# HELPER FUNCTIONS AND STRUCTURES

class record_activity_args(object):
  """
  Attributes:
   - context_id
   - visitor_id
  """

  __slots__ = [ 
    'context_id',
    'visitor_id',
   ]

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS)
      return
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.context_id = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.visitor_id = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS))
      return
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('record_activity_args')
    if self.context_id != None:
      oprot.writeFieldBegin('context_id', TType.STRING, 1)
      oprot.writeString(self.context_id.encode('utf-8')) if UTF8STRINGS and not isinstance(self.context_id, bytes) else oprot.writeString(self.context_id)
      oprot.writeFieldEnd()
    if self.visitor_id != None:
      oprot.writeFieldBegin('visitor_id', TType.STRING, 2)
      oprot.writeString(self.visitor_id.encode('utf-8')) if UTF8STRINGS and not isinstance(self.visitor_id, bytes) else oprot.writeString(self.visitor_id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = []
    for key in self.__slots__:
      padding = ' ' * (len(key) + 1)
      value = pprint.pformat(getattr(self, key))
      value = padding.join(value.splitlines(True))
      L.append('    %s=%s' % (key, value))
    return "%s(\n%s)" % (self.__class__.__name__, ",\n".join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)

all_structs.append(record_activity_args)
record_activity_args.thrift_spec = (
  None, # 0
  (1, TType.STRING, 'context_id', True, None, 2, ), # 1
  (2, TType.STRING, 'visitor_id', True, None, 2, ), # 2
)

record_activity_args.thrift_struct_annotations = {
}
record_activity_args.thrift_field_annotations = {
}

def record_activity_args__init__(self, context_id=None, visitor_id=None,):
  self.context_id = context_id
  self.visitor_id = visitor_id

record_activity_args.__init__ = record_activity_args__init__

class count_activity_args(object):
  """
  Attributes:
   - context_id
  """

  __slots__ = [ 
    'context_id',
   ]

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS)
      return
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.context_id = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS))
      return
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('count_activity_args')
    if self.context_id != None:
      oprot.writeFieldBegin('context_id', TType.STRING, 1)
      oprot.writeString(self.context_id.encode('utf-8')) if UTF8STRINGS and not isinstance(self.context_id, bytes) else oprot.writeString(self.context_id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = []
    for key in self.__slots__:
      padding = ' ' * (len(key) + 1)
      value = pprint.pformat(getattr(self, key))
      value = padding.join(value.splitlines(True))
      L.append('    %s=%s' % (key, value))
    return "%s(\n%s)" % (self.__class__.__name__, ",\n".join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)

all_structs.append(count_activity_args)
count_activity_args.thrift_spec = (
  None, # 0
  (1, TType.STRING, 'context_id', True, None, 2, ), # 1
)

count_activity_args.thrift_struct_annotations = {
}
count_activity_args.thrift_field_annotations = {
}

def count_activity_args__init__(self, context_id=None,):
  self.context_id = context_id

count_activity_args.__init__ = count_activity_args__init__

class count_activity_result(object):
  """
  Attributes:
   - success
   - invalid_context_id
  """

  __slots__ = [ 
    'success',
    'invalid_context_id',
   ]

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS)
      return
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = ActivityInfo()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.invalid_context_id = InvalidContextIDException()
          self.invalid_context_id.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS))
      return
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('count_activity_result')
    if self.success != None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.invalid_context_id != None:
      oprot.writeFieldBegin('invalid_context_id', TType.STRUCT, 1)
      self.invalid_context_id.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = []
    for key in self.__slots__:
      padding = ' ' * (len(key) + 1)
      value = pprint.pformat(getattr(self, key))
      value = padding.join(value.splitlines(True))
      L.append('    %s=%s' % (key, value))
    return "%s(\n%s)" % (self.__class__.__name__, ",\n".join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)

all_structs.append(count_activity_result)
count_activity_result.thrift_spec = (
  (0, TType.STRUCT, 'success', [ActivityInfo, ActivityInfo.thrift_spec, False], None, 2, ), # 0
  (1, TType.STRUCT, 'invalid_context_id', [InvalidContextIDException, InvalidContextIDException.thrift_spec, False], None, 2, ), # 1
)

count_activity_result.thrift_struct_annotations = {
}
count_activity_result.thrift_field_annotations = {
}

def count_activity_result__init__(self, success=None, invalid_context_id=None,):
  self.success = success
  self.invalid_context_id = invalid_context_id

count_activity_result.__init__ = count_activity_result__init__

class count_activity_multi_args(object):
  """
  Attributes:
   - context_ids
  """

  __slots__ = [ 
    'context_ids',
   ]

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS)
      return
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.context_ids = []
          (_etype3, _size0) = iprot.readListBegin()
          if _size0 >= 0:
            for _i4 in six.moves.range(_size0):
              _elem5 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
              self.context_ids.append(_elem5)
          else: 
            while iprot.peekList():
              _elem6 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
              self.context_ids.append(_elem6)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS))
      return
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('count_activity_multi_args')
    if self.context_ids != None:
      oprot.writeFieldBegin('context_ids', TType.LIST, 1)
      oprot.writeListBegin(TType.STRING, len(self.context_ids))
      for iter7 in self.context_ids:
        oprot.writeString(iter7.encode('utf-8')) if UTF8STRINGS and not isinstance(iter7, bytes) else oprot.writeString(iter7)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = []
    for key in self.__slots__:
      padding = ' ' * (len(key) + 1)
      value = pprint.pformat(getattr(self, key))
      value = padding.join(value.splitlines(True))
      L.append('    %s=%s' % (key, value))
    return "%s(\n%s)" % (self.__class__.__name__, ",\n".join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)

all_structs.append(count_activity_multi_args)
count_activity_multi_args.thrift_spec = (
  None, # 0
  (1, TType.LIST, 'context_ids', (TType.STRING,True), None, 2, ), # 1
)

count_activity_multi_args.thrift_struct_annotations = {
}
count_activity_multi_args.thrift_field_annotations = {
}

def count_activity_multi_args__init__(self, context_ids=None,):
  self.context_ids = context_ids

count_activity_multi_args.__init__ = count_activity_multi_args__init__

class count_activity_multi_result(object):
  """
  Attributes:
   - success
   - invalid_context_id
  """

  __slots__ = [ 
    'success',
    'invalid_context_id',
   ]

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS)
      return
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.MAP:
          self.success = {}
          (_ktype9, _vtype10, _size8 ) = iprot.readMapBegin() 
          if _size8 >= 0:
            for _i12 in six.moves.range(_size8):
              _key13 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
              _val14 = ActivityInfo()
              _val14.read(iprot)
              self.success[_key13] = _val14
          else: 
            while iprot.peekMap():
              _key15 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
              _val16 = ActivityInfo()
              _val16.read(iprot)
              self.success[_key15] = _val16
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.invalid_context_id = InvalidContextIDException()
          self.invalid_context_id.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS))
      return
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('count_activity_multi_result')
    if self.success != None:
      oprot.writeFieldBegin('success', TType.MAP, 0)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.success))
      for kiter17,viter18 in self.success.items():
        oprot.writeString(kiter17.encode('utf-8')) if UTF8STRINGS and not isinstance(kiter17, bytes) else oprot.writeString(kiter17)
        viter18.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.invalid_context_id != None:
      oprot.writeFieldBegin('invalid_context_id', TType.STRUCT, 1)
      self.invalid_context_id.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = []
    for key in self.__slots__:
      padding = ' ' * (len(key) + 1)
      value = pprint.pformat(getattr(self, key))
      value = padding.join(value.splitlines(True))
      L.append('    %s=%s' % (key, value))
    return "%s(\n%s)" % (self.__class__.__name__, ",\n".join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)

all_structs.append(count_activity_multi_result)
count_activity_multi_result.thrift_spec = (
  (0, TType.MAP, 'success', (TType.STRING,True,TType.STRUCT,[ActivityInfo, ActivityInfo.thrift_spec, False]), None, 2, ), # 0
  (1, TType.STRUCT, 'invalid_context_id', [InvalidContextIDException, InvalidContextIDException.thrift_spec, False], None, 2, ), # 1
)

count_activity_multi_result.thrift_struct_annotations = {
}
count_activity_multi_result.thrift_field_annotations = {
}

def count_activity_multi_result__init__(self, success=None, invalid_context_id=None,):
  self.success = success
  self.invalid_context_id = invalid_context_id

count_activity_multi_result.__init__ = count_activity_multi_result__init__

class Client(baseplate.thrift.BaseplateService.Client, Iface):
  def __init__(self, iprot, oprot=None):
    baseplate.thrift.BaseplateService.Client.__init__(self, iprot, oprot)

  def record_activity(self, context_id=None, visitor_id=None):
    """
    Register a visitor's activity within a given context.
    
    The visitor's activity will be recorded but will expire over time. If the
    user continues to be active within the context, this endpoint should be
    called occasionally to ensure they continue to be counted.
    
    This method is `oneway`; no indication of success or failure is returned.
    
    
    Parameters:
     - context_id
     - visitor_id
    """
    self.send_record_activity(context_id, visitor_id)

  def send_record_activity(self, context_id=None, visitor_id=None):
    self._oprot.writeMessageBegin('record_activity', TMessageType.CALL, self._seqid)
    args = record_activity_args()
    args.context_id = context_id
    args.visitor_id = visitor_id
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.onewayFlush()
  def count_activity(self, context_id=None):
    """
    Count how many visitors are currently active in a given context.
    
    The results of this call are cached for a period of time to ensure that if
    the count is fuzzed, the fuzzing is stable. This prevents repeated requests
    from revealing the range of fuzzing and therefore the true value.
    
    
    Parameters:
     - context_id
    """
    self.send_count_activity(context_id)
    return self.recv_count_activity()

  def send_count_activity(self, context_id=None):
    self._oprot.writeMessageBegin('count_activity', TMessageType.CALL, self._seqid)
    args = count_activity_args()
    args.context_id = context_id
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_count_activity(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = count_activity_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success != None:
      return result.success
    if result.invalid_context_id != None:
      raise result.invalid_context_id
    raise TApplicationException(TApplicationException.MISSING_RESULT, "count_activity failed: unknown result");

  def count_activity_multi(self, context_ids=None):
    """
    Count how many visitors are active in a number of given contexts.
    
    This is the same as `count_activity` but allows for querying in batch.
    
    
    Parameters:
     - context_ids
    """
    self.send_count_activity_multi(context_ids)
    return self.recv_count_activity_multi()

  def send_count_activity_multi(self, context_ids=None):
    self._oprot.writeMessageBegin('count_activity_multi', TMessageType.CALL, self._seqid)
    args = count_activity_multi_args()
    args.context_ids = context_ids
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_count_activity_multi(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = count_activity_multi_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success != None:
      return result.success
    if result.invalid_context_id != None:
      raise result.invalid_context_id
    raise TApplicationException(TApplicationException.MISSING_RESULT, "count_activity_multi failed: unknown result");


class Processor(baseplate.thrift.BaseplateService.Processor, Iface, TProcessor):
  def __init__(self, handler):
    baseplate.thrift.BaseplateService.Processor.__init__(self, handler)
    self._processMap["record_activity"] = Processor.process_record_activity
    self._processMap["count_activity"] = Processor.process_count_activity
    self._processMap["count_activity_multi"] = Processor.process_count_activity_multi

  @process_main()
  def process(self,): pass

  @process_method(record_activity_args, oneway=True)
  def process_record_activity(self, args, handler_ctx):
    try:
      self._handler.record_activity(args.context_id, args.visitor_id)
    except:
      ex = sys.exc_info()[1]
      self._event_handler.handlerError(handler_ctx, 'record_activity', ex)
      result = Thrift.TApplicationException(message=str(ex))

  @process_method(count_activity_args, oneway=False)
  def process_count_activity(self, args, handler_ctx):
    result = count_activity_result()
    try:
      result.success = self._handler.count_activity(args.context_id)
    except InvalidContextIDException as exc0:
      self._event_handler.handlerException(handler_ctx, 'count_activity', exc0)
      result.invalid_context_id = exc0
    except:
      ex = sys.exc_info()[1]
      self._event_handler.handlerError(handler_ctx, 'count_activity', ex)
      result = Thrift.TApplicationException(message=str(ex))
    return result

  @process_method(count_activity_multi_args, oneway=False)
  def process_count_activity_multi(self, args, handler_ctx):
    result = count_activity_multi_result()
    try:
      result.success = self._handler.count_activity_multi(args.context_ids)
    except InvalidContextIDException as exc0:
      self._event_handler.handlerException(handler_ctx, 'count_activity_multi', exc0)
      result.invalid_context_id = exc0
    except:
      ex = sys.exc_info()[1]
      self._event_handler.handlerError(handler_ctx, 'count_activity_multi', ex)
      result = Thrift.TApplicationException(message=str(ex))
    return result

Iface._processor_type = Processor

class ContextProcessor(baseplate.thrift.BaseplateService.ContextProcessor, ContextIface, TProcessor):
  def __init__(self, handler):
    baseplate.thrift.BaseplateService.ContextProcessor.__init__(self, handler)
    self._processMap["record_activity"] = ContextProcessor.process_record_activity
    self._processMap["count_activity"] = ContextProcessor.process_count_activity
    self._processMap["count_activity_multi"] = ContextProcessor.process_count_activity_multi

  @process_main()
  def process(self,): pass

  @process_method(record_activity_args, oneway=True)
  def process_record_activity(self, args, handler_ctx):
    try:
      self._handler.record_activity(handler_ctx, args.context_id, args.visitor_id)
    except:
      ex = sys.exc_info()[1]
      self._event_handler.handlerError(handler_ctx, 'record_activity', ex)
      result = Thrift.TApplicationException(message=str(ex))

  @process_method(count_activity_args, oneway=False)
  def process_count_activity(self, args, handler_ctx):
    result = count_activity_result()
    try:
      result.success = self._handler.count_activity(handler_ctx, args.context_id)
    except InvalidContextIDException as exc0:
      self._event_handler.handlerException(handler_ctx, 'count_activity', exc0)
      result.invalid_context_id = exc0
    except:
      ex = sys.exc_info()[1]
      self._event_handler.handlerError(handler_ctx, 'count_activity', ex)
      result = Thrift.TApplicationException(message=str(ex))
    return result

  @process_method(count_activity_multi_args, oneway=False)
  def process_count_activity_multi(self, args, handler_ctx):
    result = count_activity_multi_result()
    try:
      result.success = self._handler.count_activity_multi(handler_ctx, args.context_ids)
    except InvalidContextIDException as exc0:
      self._event_handler.handlerException(handler_ctx, 'count_activity_multi', exc0)
      result.invalid_context_id = exc0
    except:
      ex = sys.exc_info()[1]
      self._event_handler.handlerError(handler_ctx, 'count_activity_multi', ex)
      result = Thrift.TApplicationException(message=str(ex))
    return result

ContextIface._processor_type = ContextProcessor

fix_spec(all_structs)
del all_structs

