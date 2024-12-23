# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


from enum import IntEnum
import pandas



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _griddb_python
else:
    import _griddb_python

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



class ContainerType(IntEnum):
    def __int__(self):
        return self._value
    COLLECTION = 0
    TIME_SERIES = 1
class IndexType(IntEnum):
    def __int__(self):
        return int(self.value)
    DEFAULT = -1
    TREE = 1 << 0
    HASH = 1 << 1
    SPATIAL = 1 << 2
class RowSetType(IntEnum):
    def __int__(self):
        return int(self.value)
    CONTAINER_ROWS = 0
    AGGREGATION_RESULT = 1
    QUERY_ANALYSIS = 2
class FetchOption(IntEnum):
    def __int__(self):
        return int(self.value)
    LIMIT = 0

#if GS_INTERNAL_DEFINITION_VISIBLE
#if !GS_COMPATIBILITY_DEPRECATE_FETCH_OPTION_SIZE
    SIZE = (LIMIT + 1)
#endif
#endif
#if GS_COMPATIBILITY_SUPPORT_4_0
    PARTIAL_EXECUTION = (LIMIT + 2)
#endif
class TimeUnit(IntEnum):
    def __int__(self):
        return int(self.value)
    YEAR = 0
    MONTH = 1
    DAY = 2
    HOUR = 3
    MINUTE = 4
    SECOND = 5
    MILLISECOND = 6
class Type(IntEnum):
    def __int__(self):
        return self._value
    STRING = 0
    BOOL = 1
    BYTE = 2
    SHORT = 3
    INTEGER = 4
    LONG = 5
    FLOAT = 6
    DOUBLE = 7
    TIMESTAMP = 8
    GEOMETRY = 9
    BLOB = 10
    STRING_ARRAY = 11
    BOOL_ARRAY = 12
    BYTE_ARRAY = 13
    SHORT_ARRAY = 14
    INTEGER_ARRAY = 15
    LONG_ARRAY = 16
    FLOAT_ARRAY = 17
    DOUBLE_ARRAY = 18
    TIMESTAMP_ARRAY = 19
    NULL = -1

class TypeOption(IntEnum):
    def __int__(self):
        return int(self.value)
    NULLABLE = 1 << 1
    NOT_NULL = 1 << 2

class QueryOrder(IntEnum):
    def __int__(self):
        return int(self.value)
    ASCENDING = 0
    DESCENDING = 1

class Aggregation(IntEnum):
    def __int__(self):
        return int(self.value)
    MINIMUM = 0
    MAXIMUM = 1	
    TOTAL = 2
    AVERAGE = 3
    VARIANCE = 4
    STANDARD_DEVIATION = 5
    COUNT = 6
    WEIGHTED_AVERAGE = 7

class InterpolationMode(IntEnum):
    def __int__(self):
        return int(self.value)
    LINEAR_OR_PREVIOUS = 0
    EMPTY = 1

UTC_TIMESTAMP_MAX = _griddb_python.UTC_TIMESTAMP_MAX
class SwigPyIterator(object):
    r"""Proxy of C++ swig::SwigPyIterator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _griddb_python.delete_SwigPyIterator

    def value(self):
        r"""value(self) -> PyObject *"""
        return _griddb_python.SwigPyIterator_value(self)

    def incr(self, n=1):
        r"""incr(self, n=1) -> SwigPyIterator"""
        return _griddb_python.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        r"""decr(self, n=1) -> SwigPyIterator"""
        return _griddb_python.SwigPyIterator_decr(self, n)

    def distance(self, x):
        r"""distance(self, x) -> ptrdiff_t"""
        return _griddb_python.SwigPyIterator_distance(self, x)

    def equal(self, x):
        r"""equal(self, x) -> bool"""
        return _griddb_python.SwigPyIterator_equal(self, x)

    def copy(self):
        r"""copy(self) -> SwigPyIterator"""
        return _griddb_python.SwigPyIterator_copy(self)

    def next(self):
        r"""next(self) -> PyObject *"""
        return _griddb_python.SwigPyIterator_next(self)

    def __next__(self):
        r"""__next__(self) -> PyObject *"""
        return _griddb_python.SwigPyIterator___next__(self)

    def previous(self):
        r"""previous(self) -> PyObject *"""
        return _griddb_python.SwigPyIterator_previous(self)

    def advance(self, n):
        r"""advance(self, n) -> SwigPyIterator"""
        return _griddb_python.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        r"""__eq__(self, x) -> bool"""
        return _griddb_python.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        r"""__ne__(self, x) -> bool"""
        return _griddb_python.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        r"""__iadd__(self, n) -> SwigPyIterator"""
        return _griddb_python.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        r"""__isub__(self, n) -> SwigPyIterator"""
        return _griddb_python.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        r"""__add__(self, n) -> SwigPyIterator"""
        return _griddb_python.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        r"""
        __sub__(self, n) -> SwigPyIterator
        __sub__(self, x) -> ptrdiff_t
        """
        return _griddb_python.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _griddb_python:
_griddb_python.SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _griddb_python.SHARED_PTR_DISOWN

GS_CONTAINER_COLLECTION = _griddb_python.GS_CONTAINER_COLLECTION

GS_CONTAINER_TIME_SERIES = _griddb_python.GS_CONTAINER_TIME_SERIES

GS_ROW_SET_CONTAINER_ROWS = _griddb_python.GS_ROW_SET_CONTAINER_ROWS

GS_ROW_SET_AGGREGATION_RESULT = _griddb_python.GS_ROW_SET_AGGREGATION_RESULT

GS_ROW_SET_QUERY_ANALYSIS = _griddb_python.GS_ROW_SET_QUERY_ANALYSIS

GS_TYPE_STRING = _griddb_python.GS_TYPE_STRING

GS_TYPE_BOOL = _griddb_python.GS_TYPE_BOOL

GS_TYPE_BYTE = _griddb_python.GS_TYPE_BYTE

GS_TYPE_SHORT = _griddb_python.GS_TYPE_SHORT

GS_TYPE_INTEGER = _griddb_python.GS_TYPE_INTEGER

GS_TYPE_LONG = _griddb_python.GS_TYPE_LONG

GS_TYPE_FLOAT = _griddb_python.GS_TYPE_FLOAT

GS_TYPE_DOUBLE = _griddb_python.GS_TYPE_DOUBLE

GS_TYPE_TIMESTAMP = _griddb_python.GS_TYPE_TIMESTAMP

GS_TYPE_GEOMETRY = _griddb_python.GS_TYPE_GEOMETRY

GS_TYPE_BLOB = _griddb_python.GS_TYPE_BLOB

GS_TYPE_STRING_ARRAY = _griddb_python.GS_TYPE_STRING_ARRAY

GS_TYPE_BOOL_ARRAY = _griddb_python.GS_TYPE_BOOL_ARRAY

GS_TYPE_BYTE_ARRAY = _griddb_python.GS_TYPE_BYTE_ARRAY

GS_TYPE_SHORT_ARRAY = _griddb_python.GS_TYPE_SHORT_ARRAY

GS_TYPE_INTEGER_ARRAY = _griddb_python.GS_TYPE_INTEGER_ARRAY

GS_TYPE_LONG_ARRAY = _griddb_python.GS_TYPE_LONG_ARRAY

GS_TYPE_FLOAT_ARRAY = _griddb_python.GS_TYPE_FLOAT_ARRAY

GS_TYPE_DOUBLE_ARRAY = _griddb_python.GS_TYPE_DOUBLE_ARRAY

GS_TYPE_TIMESTAMP_ARRAY = _griddb_python.GS_TYPE_TIMESTAMP_ARRAY

GS_TYPE_NULL = _griddb_python.GS_TYPE_NULL

GS_INDEX_FLAG_DEFAULT = _griddb_python.GS_INDEX_FLAG_DEFAULT

GS_INDEX_FLAG_TREE = _griddb_python.GS_INDEX_FLAG_TREE

GS_INDEX_FLAG_HASH = _griddb_python.GS_INDEX_FLAG_HASH

GS_INDEX_FLAG_SPATIAL = _griddb_python.GS_INDEX_FLAG_SPATIAL

GS_FETCH_LIMIT = _griddb_python.GS_FETCH_LIMIT

GS_TIME_UNIT_YEAR = _griddb_python.GS_TIME_UNIT_YEAR

GS_TIME_UNIT_MONTH = _griddb_python.GS_TIME_UNIT_MONTH

GS_TIME_UNIT_DAY = _griddb_python.GS_TIME_UNIT_DAY

GS_TIME_UNIT_HOUR = _griddb_python.GS_TIME_UNIT_HOUR

GS_TIME_UNIT_MINUTE = _griddb_python.GS_TIME_UNIT_MINUTE

GS_TIME_UNIT_SECOND = _griddb_python.GS_TIME_UNIT_SECOND

GS_TIME_UNIT_MILLISECOND = _griddb_python.GS_TIME_UNIT_MILLISECOND

GS_TYPE_OPTION_KEY = _griddb_python.GS_TYPE_OPTION_KEY

GS_TYPE_OPTION_NULLABLE = _griddb_python.GS_TYPE_OPTION_NULLABLE

GS_TYPE_OPTION_NOT_NULL = _griddb_python.GS_TYPE_OPTION_NOT_NULL

DEFAULT_ERROR_CODE = _griddb_python.DEFAULT_ERROR_CODE

DEFAULT_ERROR_STACK_SIZE = _griddb_python.DEFAULT_ERROR_STACK_SIZE

class GSException(Exception):
    r"""Proxy of C++ griddb::GSException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _griddb_python.delete_GSException

    def close(self):
        r"""close(self)"""
        return _griddb_python.GSException_close(self)

    def get_code(self):
        r"""get_code(self) -> int32_t"""
        return _griddb_python.GSException_get_code(self)

    def what(self):
        r"""what(self) -> char const *"""
        return _griddb_python.GSException_what(self)

    def get_error_stack_size(self):
        r"""get_error_stack_size(self) -> size_t"""
        return _griddb_python.GSException_get_error_stack_size(self)

    def get_error_code(self, stack_index):
        r"""get_error_code(self, stack_index) -> GSResult"""
        return _griddb_python.GSException_get_error_code(self, stack_index)

    def get_message(self, stack_index, buf_size=1024):
        r"""get_message(self, stack_index, buf_size=1024) -> std::string"""
        return _griddb_python.GSException_get_message(self, stack_index, buf_size)

    def get_location(self, stack_index, buf_size=1024):
        r"""get_location(self, stack_index, buf_size=1024) -> std::string"""
        return _griddb_python.GSException_get_location(self, stack_index, buf_size)
    is_timeout = property(_griddb_python.GSException_is_timeout_get, doc=r"""is_timeout""")

# Register GSException in _griddb_python:
_griddb_python.GSException_swigregister(GSException)

class AggregationResult(object):
    r"""Proxy of C++ griddb::AggregationResult class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    timestamp_output_with_float = property(_griddb_python.AggregationResult_timestamp_output_with_float_get, _griddb_python.AggregationResult_timestamp_output_with_float_set, doc=r"""timestamp_output_with_float""")
    __swig_destroy__ = _griddb_python.delete_AggregationResult

    def close(self):
        r"""close(self)"""
        return _griddb_python.AggregationResult_close(self)

    def get(self, type):
        r"""get(self, type)"""
        return _griddb_python.AggregationResult_get(self, type)

# Register AggregationResult in _griddb_python:
_griddb_python.AggregationResult_swigregister(AggregationResult)

class ExpirationInfo(object):
    r"""Proxy of C++ griddb::ExpirationInfo class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, timeSeriesProps) -> ExpirationInfo
        __init__(self, time, unit, division_count) -> ExpirationInfo
        """
        _griddb_python.ExpirationInfo_swiginit(self, _griddb_python.new_ExpirationInfo(*args))
    __swig_destroy__ = _griddb_python.delete_ExpirationInfo

    def gs_ts(self):
        r"""gs_ts(self) -> GSTimeSeriesProperties *"""
        return _griddb_python.ExpirationInfo_gs_ts(self)
    time = property(_griddb_python.ExpirationInfo_time_get, _griddb_python.ExpirationInfo_time_set, doc=r"""time""")
    unit = property(_griddb_python.ExpirationInfo_unit_get, _griddb_python.ExpirationInfo_unit_set, doc=r"""unit""")
    division_count = property(_griddb_python.ExpirationInfo_division_count_get, _griddb_python.ExpirationInfo_division_count_set, doc=r"""division_count""")

# Register ExpirationInfo in _griddb_python:
_griddb_python.ExpirationInfo_swigregister(ExpirationInfo)

class ColumnInfoList(object):
    r"""Proxy of C++ ColumnInfoList class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    columnInfo = property(_griddb_python.ColumnInfoList_columnInfo_get, _griddb_python.ColumnInfoList_columnInfo_set, doc=r"""columnInfo""")
    size = property(_griddb_python.ColumnInfoList_size_get, _griddb_python.ColumnInfoList_size_set, doc=r"""size""")

    def __init__(self):
        r"""__init__(self) -> ColumnInfoList"""
        _griddb_python.ColumnInfoList_swiginit(self, _griddb_python.new_ColumnInfoList())
    __swig_destroy__ = _griddb_python.delete_ColumnInfoList

# Register ColumnInfoList in _griddb_python:
_griddb_python.ColumnInfoList_swigregister(ColumnInfoList)

class ContainerInfo(object):
    r"""Proxy of C++ griddb::ContainerInfo class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, name, column_info_list, type=GS_CONTAINER_COLLECTION, row_key=True, expiration=None, dataAffinity=None):
        r"""__init__(self, name, column_info_list, type=GS_CONTAINER_COLLECTION, row_key=True, expiration=None, dataAffinity=None) -> ContainerInfo"""
        _griddb_python.ContainerInfo_swiginit(self, _griddb_python.new_ContainerInfo(name, column_info_list, type, row_key, expiration, dataAffinity))
    __swig_destroy__ = _griddb_python.delete_ContainerInfo

    def get_column_info(self, column):
        r"""get_column_info(self, column) -> GSColumnInfo"""
        return _griddb_python.ContainerInfo_get_column_info(self, column)
    name = property(_griddb_python.ContainerInfo_name_get, _griddb_python.ContainerInfo_name_set, doc=r"""name""")
    type = property(_griddb_python.ContainerInfo_type_get, _griddb_python.ContainerInfo_type_set, doc=r"""type""")
    row_key = property(_griddb_python.ContainerInfo_row_key_get, _griddb_python.ContainerInfo_row_key_set, doc=r"""row_key""")
    expiration = property(_griddb_python.ContainerInfo_expiration_get, _griddb_python.ContainerInfo_expiration_set, doc=r"""expiration""")
    column_info_list = property(_griddb_python.ContainerInfo_column_info_list_get, _griddb_python.ContainerInfo_column_info_list_set, doc=r"""column_info_list""")
    dataAffinity = property(_griddb_python.ContainerInfo_dataAffinity_get, _griddb_python.ContainerInfo_dataAffinity_set, doc=r"""dataAffinity""")

# Register ContainerInfo in _griddb_python:
_griddb_python.ContainerInfo_swigregister(ContainerInfo)

class QueryAnalysisEntry(object):
    r"""Proxy of C++ griddb::QueryAnalysisEntry class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _griddb_python.delete_QueryAnalysisEntry

    def close(self):
        r"""close(self)"""
        return _griddb_python.QueryAnalysisEntry_close(self)

    def get(self):
        r"""get(self)"""
        return _griddb_python.QueryAnalysisEntry_get(self)

# Register QueryAnalysisEntry in _griddb_python:
_griddb_python.QueryAnalysisEntry_swigregister(QueryAnalysisEntry)

class RowSet(object):
    r"""Proxy of C++ griddb::RowSet class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    timestamp_output_with_float = property(_griddb_python.RowSet_timestamp_output_with_float_get, _griddb_python.RowSet_timestamp_output_with_float_set, doc=r"""timestamp_output_with_float""")
    __swig_destroy__ = _griddb_python.delete_RowSet

    def close(self):
        r"""close(self)"""
        return _griddb_python.RowSet_close(self)

    def has_next(self):
        r"""has_next(self) -> bool"""
        return _griddb_python.RowSet_has_next(self)

    def next(self):
        r"""next(self)"""
        return _griddb_python.RowSet_next(self)

    def update(self, row):
        r"""update(self, row)"""
        return _griddb_python.RowSet_update(self, row)

    def remove(self):
        r"""remove(self)"""
        return _griddb_python.RowSet_remove(self)

    def get_column_names(self):
        r"""get_column_names(self)"""
        return _griddb_python.RowSet_get_column_names(self)

    def fetch_rows(self):
        r"""fetch_rows(self) -> RowList"""
        val = _griddb_python.RowSet_fetch_rows(self)

            #convert data from numpy.ndarray to pandas.DataFrame
            #"val" is output
        columnsList = self.get_column_names()
        val = pandas.DataFrame(val, columns = columnsList)


        return val


    def __iter__(self):
        r"""__iter__(self) -> RowSet"""
        return _griddb_python.RowSet___iter__(self)

    def __next__(self):
        r"""__next__(self)"""
        return _griddb_python.RowSet___next__(self)
    size = property(_griddb_python.RowSet_size_get, doc=r"""size""")
    type = property(_griddb_python.RowSet_type_get, doc=r"""type""")

# Register RowSet in _griddb_python:
_griddb_python.RowSet_swigregister(RowSet)

class Query(object):
    r"""Proxy of C++ griddb::Query class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _griddb_python.delete_Query

    def close(self):
        r"""close(self)"""
        return _griddb_python.Query_close(self)

    def fetch(self, for_update=False):
        r"""fetch(self, for_update=False) -> RowSet"""
        return _griddb_python.Query_fetch(self, for_update)

    def set_fetch_options(self, limit=-1, partial=False):
        r"""set_fetch_options(self, limit=-1, partial=False)"""
        return _griddb_python.Query_set_fetch_options(self, limit, partial)

    def get_row_set(self):
        r"""get_row_set(self) -> RowSet"""
        return _griddb_python.Query_get_row_set(self)

# Register Query in _griddb_python:
_griddb_python.Query_swigregister(Query)

class Container(object):
    r"""Proxy of C++ griddb::Container class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    timestamp_output_with_float = property(_griddb_python.Container_timestamp_output_with_float_get, _griddb_python.Container_timestamp_output_with_float_set, doc=r"""timestamp_output_with_float""")
    __swig_destroy__ = _griddb_python.delete_Container

    def close(self, *args):
        r"""close(self, allRelated=GS_FALSE)"""
        return _griddb_python.Container_close(self, *args)

    def create_index(self, column_name, index_type=GS_INDEX_FLAG_DEFAULT, name=None):
        r"""create_index(self, column_name, index_type=GS_INDEX_FLAG_DEFAULT, name=None)"""
        return _griddb_python.Container_create_index(self, column_name, index_type, name)

    def drop_index(self, column_name, index_type=GS_INDEX_FLAG_DEFAULT, name=None):
        r"""drop_index(self, column_name, index_type=GS_INDEX_FLAG_DEFAULT, name=None)"""
        return _griddb_python.Container_drop_index(self, column_name, index_type, name)

    def put(self, row):
        r"""put(self, row) -> bool"""
        return _griddb_python.Container_put(self, row)

    def query(self, query):
        r"""query(self, query) -> Query"""
        return _griddb_python.Container_query(self, query)

    def abort(self):
        r"""abort(self)"""
        return _griddb_python.Container_abort(self)

    def flush(self):
        r"""flush(self)"""
        return _griddb_python.Container_flush(self)

    def set_auto_commit(self, enabled):
        r"""set_auto_commit(self, enabled)"""
        return _griddb_python.Container_set_auto_commit(self, enabled)

    def commit(self):
        r"""commit(self)"""
        return _griddb_python.Container_commit(self)

    def get(self, key):
        r"""get(self, key) -> GSBool"""
        return _griddb_python.Container_get(self, key)

    def remove(self, key):
        r"""remove(self, key) -> bool"""
        return _griddb_python.Container_remove(self, key)

    def multi_put(self, row_list):
        r"""multi_put(self, row_list)"""
        return _griddb_python.Container_multi_put(self, row_list)

    def put_rows(self, listRow):
        r"""put_rows(self, listRow)"""

            # listRow is input
        if isinstance(listRow, pandas.DataFrame) != True:
            raise Exception('Input should be DataFrame')
        # Convert to numpy ndarray
        listRow = listRow.to_numpy()


        return _griddb_python.Container_put_rows(self, listRow)


    def query_by_time_series_range(self, *args):
        r"""query_by_time_series_range(self, startTime, endTime, order=GS_ORDER_ASCENDING) -> Query"""
        return _griddb_python.Container_query_by_time_series_range(self, *args)

    def aggregate_time_series(self, startTime, endTime, aggregation, column=None):
        r"""aggregate_time_series(self, startTime, endTime, aggregation, column=None) -> AggregationResult"""
        return _griddb_python.Container_aggregate_time_series(self, startTime, endTime, aggregation, column)

    def query_by_time_series_sampling(self, startTime, endTime, columnSet, mode, interval, intervalUnit):
        r"""query_by_time_series_sampling(self, startTime, endTime, columnSet, mode, interval, intervalUnit) -> Query"""
        return _griddb_python.Container_query_by_time_series_sampling(self, startTime, endTime, columnSet, mode, interval, intervalUnit)
    type = property(_griddb_python.Container_type_get, doc=r"""type""")

# Register Container in _griddb_python:
_griddb_python.Container_swigregister(Container)

class PartitionController(object):
    r"""Proxy of C++ griddb::PartitionController class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _griddb_python.delete_PartitionController

    def close(self):
        r"""close(self)"""
        return _griddb_python.PartitionController_close(self)

    def get_container_count(self, partition_index):
        r"""get_container_count(self, partition_index) -> int64_t"""
        return _griddb_python.PartitionController_get_container_count(self, partition_index)

    def get_container_names(self, partition_index, start, limit=-1):
        r"""get_container_names(self, partition_index, start, limit=-1)"""
        return _griddb_python.PartitionController_get_container_names(self, partition_index, start, limit)

    def get_partition_index_of_container(self, container_name):
        r"""get_partition_index_of_container(self, container_name) -> int32_t"""
        return _griddb_python.PartitionController_get_partition_index_of_container(self, container_name)
    partition_count = property(_griddb_python.PartitionController_partition_count_get, doc=r"""partition_count""")

# Register PartitionController in _griddb_python:
_griddb_python.PartitionController_swigregister(PartitionController)

class RowKeyPredicate(object):
    r"""Proxy of C++ griddb::RowKeyPredicate class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    timestamp_output_with_float = property(_griddb_python.RowKeyPredicate_timestamp_output_with_float_get, _griddb_python.RowKeyPredicate_timestamp_output_with_float_set, doc=r"""timestamp_output_with_float""")
    __swig_destroy__ = _griddb_python.delete_RowKeyPredicate

    def close(self):
        r"""close(self)"""
        return _griddb_python.RowKeyPredicate_close(self)

    def get_range(self):
        r"""get_range(self)"""
        return _griddb_python.RowKeyPredicate_get_range(self)

    def set_range(self, start, end):
        r"""set_range(self, start, end)"""
        return _griddb_python.RowKeyPredicate_set_range(self, start, end)

    def set_distinct_keys(self, keys):
        r"""set_distinct_keys(self, keys)"""
        return _griddb_python.RowKeyPredicate_set_distinct_keys(self, keys)

    def get_distinct_keys(self):
        r"""get_distinct_keys(self)"""
        return _griddb_python.RowKeyPredicate_get_distinct_keys(self)
    key_type = property(_griddb_python.RowKeyPredicate_key_type_get, doc=r"""key_type""")

# Register RowKeyPredicate in _griddb_python:
_griddb_python.RowKeyPredicate_swigregister(RowKeyPredicate)

class Store(object):
    r"""Proxy of C++ griddb::Store class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    timestamp_output_with_float = property(_griddb_python.Store_timestamp_output_with_float_get, _griddb_python.Store_timestamp_output_with_float_set, doc=r"""timestamp_output_with_float""")
    __swig_destroy__ = _griddb_python.delete_Store

    def close(self, *args):
        r"""close(self, allRelated=GS_FALSE)"""
        return _griddb_python.Store_close(self, *args)

    def put_container(self, info, modifiable=False):
        r"""put_container(self, info, modifiable=False) -> Container"""
        return _griddb_python.Store_put_container(self, info, modifiable)

    def get_container(self, name):
        r"""get_container(self, name) -> Container"""
        return _griddb_python.Store_get_container(self, name)

    def drop_container(self, name):
        r"""drop_container(self, name)"""
        return _griddb_python.Store_drop_container(self, name)

    def fetch_all(self, query_list):
        r"""fetch_all(self, query_list)"""
        return _griddb_python.Store_fetch_all(self, query_list)

    def multi_put(self, container_entry):
        r"""multi_put(self, container_entry)"""
        return _griddb_python.Store_multi_put(self, container_entry)

    def multi_get(self, predicateList):
        r"""multi_get(self, predicateList)"""
        return _griddb_python.Store_multi_get(self, predicateList)

    def get_container_info(self, name):
        r"""get_container_info(self, name) -> ContainerInfo"""
        return _griddb_python.Store_get_container_info(self, name)

    def create_row_key_predicate(self, type):
        r"""create_row_key_predicate(self, type) -> RowKeyPredicate"""
        return _griddb_python.Store_create_row_key_predicate(self, type)
    partition_info = property(_griddb_python.Store_partition_info_get, doc=r"""partition_info""")

# Register Store in _griddb_python:
_griddb_python.Store_swigregister(Store)

CLIENT_VERSION = _griddb_python.CLIENT_VERSION

class StoreFactory(object):
    r"""Proxy of C++ griddb::StoreFactory class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _griddb_python.delete_StoreFactory

    def close(self, *args):
        r"""close(self, allRelated=GS_FALSE)"""
        return _griddb_python.StoreFactory_close(self, *args)

    @staticmethod
    def get_instance():
        r"""get_instance() -> StoreFactory"""
        return _griddb_python.StoreFactory_get_instance()

    def get_store(self, host=None, port=0, cluster_name=None, database=None, username=None, password=None, notification_member=None, notification_provider=None):
        r"""get_store(self, host=None, port=0, cluster_name=None, database=None, username=None, password=None, notification_member=None, notification_provider=None) -> Store"""
        return _griddb_python.StoreFactory_get_store(self, host, port, cluster_name, database, username, password, notification_member, notification_provider)

    def get_version(self):
        r"""get_version(self) -> std::string"""
        return _griddb_python.StoreFactory_get_version(self)

# Register StoreFactory in _griddb_python:
_griddb_python.StoreFactory_swigregister(StoreFactory)

def StoreFactory_get_instance():
    r"""StoreFactory_get_instance() -> StoreFactory"""
    return _griddb_python.StoreFactory_get_instance()

class RowList(object):
    r"""Proxy of C++ griddb::RowList class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, gsRow, gsRowSet, typelist, columnCount, timetampFloat):
        r"""__init__(self, gsRow, gsRowSet, typelist, columnCount, timetampFloat) -> RowList"""
        _griddb_python.RowList_swiginit(self, _griddb_python.new_RowList(gsRow, gsRowSet, typelist, columnCount, timetampFloat))

    def __next__(self):
        r"""__next__(self)"""
        return _griddb_python.RowList___next__(self)

    def __iter__(self):
        r"""__iter__(self) -> RowList"""
        return _griddb_python.RowList___iter__(self)

    def get_gsrow_ptr(self):
        r"""get_gsrow_ptr(self) -> GSRow *"""
        return _griddb_python.RowList_get_gsrow_ptr(self)

    def get_gstype_list(self):
        r"""get_gstype_list(self) -> GSType *"""
        return _griddb_python.RowList_get_gstype_list(self)

    def get_column_count(self):
        r"""get_column_count(self) -> int"""
        return _griddb_python.RowList_get_column_count(self)

    def get_timestamp_to_float(self):
        r"""get_timestamp_to_float(self) -> bool"""
        return _griddb_python.RowList_get_timestamp_to_float(self)
    __swig_destroy__ = _griddb_python.delete_RowList

# Register RowList in _griddb_python:
_griddb_python.RowList_swigregister(RowList)

class TimestampUtils(object):
    r"""Proxy of C++ griddb::TimestampUtils class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _griddb_python.delete_TimestampUtils

    @staticmethod
    def get_time_millis(timestamp):
        r"""get_time_millis(timestamp) -> int64_t"""
        return _griddb_python.TimestampUtils_get_time_millis(timestamp)

# Register TimestampUtils in _griddb_python:
_griddb_python.TimestampUtils_swigregister(TimestampUtils)

def TimestampUtils_get_time_millis(timestamp):
    r"""TimestampUtils_get_time_millis(timestamp) -> int64_t"""
    return _griddb_python.TimestampUtils_get_time_millis(timestamp)



