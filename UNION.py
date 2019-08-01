# STRUCT and UNION are used as placeholders when defining structures; at the
# time they are defined it is not possible to determine their alignment as
# the structure in which they appear has that information and it is not yet
# (fully) defined. Once the structure in which they appear is defined, it will
# look for instances of STRUCT or UNION and replace them with real classes
# that have the right alignment.
class UNION(object):
  def __init__(oSelf, *axFields):
    oSelf.axFields = axFields;
