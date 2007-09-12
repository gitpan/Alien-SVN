# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _client

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import core
import delta
import wc
import ra

def svn_client_version(*args):
    """svn_client_version() -> svn_version_t"""
    return apply(_client.svn_client_version, args)

def svn_client_get_simple_prompt_provider(*args):
    """
    svn_client_get_simple_prompt_provider(svn_auth_provider_object_t provider, svn_auth_simple_prompt_func_t prompt_func, 
        int retry_limit, 
        apr_pool_t pool)
    """
    return apply(_client.svn_client_get_simple_prompt_provider, args)

def svn_client_get_username_prompt_provider(*args):
    """
    svn_client_get_username_prompt_provider(svn_auth_provider_object_t provider, svn_auth_username_prompt_func_t prompt_func, 
        int retry_limit, 
        apr_pool_t pool)
    """
    return apply(_client.svn_client_get_username_prompt_provider, args)

def svn_client_get_simple_provider(*args):
    """svn_client_get_simple_provider(svn_auth_provider_object_t provider, apr_pool_t pool)"""
    return apply(_client.svn_client_get_simple_provider, args)

def svn_client_get_username_provider(*args):
    """svn_client_get_username_provider(svn_auth_provider_object_t provider, apr_pool_t pool)"""
    return apply(_client.svn_client_get_username_provider, args)

def svn_client_get_ssl_server_trust_file_provider(*args):
    """svn_client_get_ssl_server_trust_file_provider(svn_auth_provider_object_t provider, apr_pool_t pool)"""
    return apply(_client.svn_client_get_ssl_server_trust_file_provider, args)

def svn_client_get_ssl_client_cert_file_provider(*args):
    """svn_client_get_ssl_client_cert_file_provider(svn_auth_provider_object_t provider, apr_pool_t pool)"""
    return apply(_client.svn_client_get_ssl_client_cert_file_provider, args)

def svn_client_get_ssl_client_cert_pw_file_provider(*args):
    """svn_client_get_ssl_client_cert_pw_file_provider(svn_auth_provider_object_t provider, apr_pool_t pool)"""
    return apply(_client.svn_client_get_ssl_client_cert_pw_file_provider, args)

def svn_client_get_ssl_server_trust_prompt_provider(*args):
    """
    svn_client_get_ssl_server_trust_prompt_provider(svn_auth_provider_object_t provider, svn_auth_ssl_server_trust_prompt_func_t prompt_func, 
        apr_pool_t pool)
    """
    return apply(_client.svn_client_get_ssl_server_trust_prompt_provider, args)

def svn_client_get_ssl_client_cert_prompt_provider(*args):
    """
    svn_client_get_ssl_client_cert_prompt_provider(svn_auth_provider_object_t provider, svn_auth_ssl_client_cert_prompt_func_t prompt_func, 
        int retry_limit, 
        apr_pool_t pool)
    """
    return apply(_client.svn_client_get_ssl_client_cert_prompt_provider, args)

def svn_client_get_ssl_client_cert_pw_prompt_provider(*args):
    """
    svn_client_get_ssl_client_cert_pw_prompt_provider(svn_auth_provider_object_t provider, svn_auth_ssl_client_cert_pw_prompt_func_t prompt_func, 
        int retry_limit, 
        apr_pool_t pool)
    """
    return apply(_client.svn_client_get_ssl_client_cert_pw_prompt_provider, args)

def svn_client_proplist_item_dup(*args):
    """svn_client_proplist_item_dup( item, apr_pool_t pool)"""
    return apply(_client.svn_client_proplist_item_dup, args)
class svn_client_commit_info_t:
    """Proxy of C svn_client_commit_info_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_client_commit_info_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_client_commit_info_t, name)
    def __repr__(self):
        return "<%s.%s; proxy of C svn_client_commit_info_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["revision"] = _client.svn_client_commit_info_t_revision_set
    __swig_getmethods__["revision"] = _client.svn_client_commit_info_t_revision_get
    __swig_setmethods__["date"] = _client.svn_client_commit_info_t_date_set
    __swig_getmethods__["date"] = _client.svn_client_commit_info_t_date_get
    __swig_setmethods__["author"] = _client.svn_client_commit_info_t_author_set
    __swig_getmethods__["author"] = _client.svn_client_commit_info_t_author_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_client_commit_info_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)

    def __init__(self, *args):
        """__init__(self) -> svn_client_commit_info_t"""
        _swig_setattr(self, svn_client_commit_info_t, 'this', apply(_client.new_svn_client_commit_info_t, args))
        _swig_setattr(self, svn_client_commit_info_t, 'thisown', 1)
    def __del__(self, destroy=_client.delete_svn_client_commit_info_t):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class svn_client_commit_info_tPtr(svn_client_commit_info_t):
    def __init__(self, this):
        _swig_setattr(self, svn_client_commit_info_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_client_commit_info_t, 'thisown', 0)
        _swig_setattr(self, svn_client_commit_info_t,self.__class__,svn_client_commit_info_t)
_client.svn_client_commit_info_t_swigregister(svn_client_commit_info_tPtr)

SVN_CLIENT_COMMIT_ITEM_ADD = _client.SVN_CLIENT_COMMIT_ITEM_ADD
SVN_CLIENT_COMMIT_ITEM_DELETE = _client.SVN_CLIENT_COMMIT_ITEM_DELETE
SVN_CLIENT_COMMIT_ITEM_TEXT_MODS = _client.SVN_CLIENT_COMMIT_ITEM_TEXT_MODS
SVN_CLIENT_COMMIT_ITEM_PROP_MODS = _client.SVN_CLIENT_COMMIT_ITEM_PROP_MODS
SVN_CLIENT_COMMIT_ITEM_IS_COPY = _client.SVN_CLIENT_COMMIT_ITEM_IS_COPY
SVN_CLIENT_COMMIT_ITEM_LOCK_TOKEN = _client.SVN_CLIENT_COMMIT_ITEM_LOCK_TOKEN
class svn_client_commit_item2_t:
    """Proxy of C svn_client_commit_item2_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_client_commit_item2_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_client_commit_item2_t, name)
    def __repr__(self):
        return "<%s.%s; proxy of C svn_client_commit_item2_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["path"] = _client.svn_client_commit_item2_t_path_set
    __swig_getmethods__["path"] = _client.svn_client_commit_item2_t_path_get
    __swig_setmethods__["kind"] = _client.svn_client_commit_item2_t_kind_set
    __swig_getmethods__["kind"] = _client.svn_client_commit_item2_t_kind_get
    __swig_setmethods__["url"] = _client.svn_client_commit_item2_t_url_set
    __swig_getmethods__["url"] = _client.svn_client_commit_item2_t_url_get
    __swig_setmethods__["revision"] = _client.svn_client_commit_item2_t_revision_set
    __swig_getmethods__["revision"] = _client.svn_client_commit_item2_t_revision_get
    __swig_setmethods__["copyfrom_url"] = _client.svn_client_commit_item2_t_copyfrom_url_set
    __swig_getmethods__["copyfrom_url"] = _client.svn_client_commit_item2_t_copyfrom_url_get
    __swig_setmethods__["copyfrom_rev"] = _client.svn_client_commit_item2_t_copyfrom_rev_set
    __swig_getmethods__["copyfrom_rev"] = _client.svn_client_commit_item2_t_copyfrom_rev_get
    __swig_setmethods__["state_flags"] = _client.svn_client_commit_item2_t_state_flags_set
    __swig_getmethods__["state_flags"] = _client.svn_client_commit_item2_t_state_flags_get
    __swig_setmethods__["wcprop_changes"] = _client.svn_client_commit_item2_t_wcprop_changes_set
    __swig_getmethods__["wcprop_changes"] = _client.svn_client_commit_item2_t_wcprop_changes_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_client_commit_item2_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)

    def __init__(self, *args):
        """__init__(self) -> svn_client_commit_item2_t"""
        _swig_setattr(self, svn_client_commit_item2_t, 'this', apply(_client.new_svn_client_commit_item2_t, args))
        _swig_setattr(self, svn_client_commit_item2_t, 'thisown', 1)
    def __del__(self, destroy=_client.delete_svn_client_commit_item2_t):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class svn_client_commit_item2_tPtr(svn_client_commit_item2_t):
    def __init__(self, this):
        _swig_setattr(self, svn_client_commit_item2_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_client_commit_item2_t, 'thisown', 0)
        _swig_setattr(self, svn_client_commit_item2_t,self.__class__,svn_client_commit_item2_t)
_client.svn_client_commit_item2_t_swigregister(svn_client_commit_item2_tPtr)


def svn_client_commit_item2_dup(*args):
    """svn_client_commit_item2_dup(svn_client_commit_item2_t item, apr_pool_t pool) -> svn_client_commit_item2_t"""
    return apply(_client.svn_client_commit_item2_dup, args)
class svn_client_commit_item_t:
    """Proxy of C svn_client_commit_item_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_client_commit_item_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_client_commit_item_t, name)
    def __repr__(self):
        return "<%s.%s; proxy of C svn_client_commit_item_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["path"] = _client.svn_client_commit_item_t_path_set
    __swig_getmethods__["path"] = _client.svn_client_commit_item_t_path_get
    __swig_setmethods__["kind"] = _client.svn_client_commit_item_t_kind_set
    __swig_getmethods__["kind"] = _client.svn_client_commit_item_t_kind_get
    __swig_setmethods__["url"] = _client.svn_client_commit_item_t_url_set
    __swig_getmethods__["url"] = _client.svn_client_commit_item_t_url_get
    __swig_setmethods__["revision"] = _client.svn_client_commit_item_t_revision_set
    __swig_getmethods__["revision"] = _client.svn_client_commit_item_t_revision_get
    __swig_setmethods__["copyfrom_url"] = _client.svn_client_commit_item_t_copyfrom_url_set
    __swig_getmethods__["copyfrom_url"] = _client.svn_client_commit_item_t_copyfrom_url_get
    __swig_setmethods__["state_flags"] = _client.svn_client_commit_item_t_state_flags_set
    __swig_getmethods__["state_flags"] = _client.svn_client_commit_item_t_state_flags_get
    __swig_setmethods__["wcprop_changes"] = _client.svn_client_commit_item_t_wcprop_changes_set
    __swig_getmethods__["wcprop_changes"] = _client.svn_client_commit_item_t_wcprop_changes_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_client_commit_item_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)

    def __init__(self, *args):
        """__init__(self) -> svn_client_commit_item_t"""
        _swig_setattr(self, svn_client_commit_item_t, 'this', apply(_client.new_svn_client_commit_item_t, args))
        _swig_setattr(self, svn_client_commit_item_t, 'thisown', 1)
    def __del__(self, destroy=_client.delete_svn_client_commit_item_t):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class svn_client_commit_item_tPtr(svn_client_commit_item_t):
    def __init__(self, this):
        _swig_setattr(self, svn_client_commit_item_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_client_commit_item_t, 'thisown', 0)
        _swig_setattr(self, svn_client_commit_item_t,self.__class__,svn_client_commit_item_t)
_client.svn_client_commit_item_t_swigregister(svn_client_commit_item_tPtr)

svn_client_diff_summarize_kind_normal = _client.svn_client_diff_summarize_kind_normal
svn_client_diff_summarize_kind_added = _client.svn_client_diff_summarize_kind_added
svn_client_diff_summarize_kind_modified = _client.svn_client_diff_summarize_kind_modified
svn_client_diff_summarize_kind_deleted = _client.svn_client_diff_summarize_kind_deleted
class svn_client_diff_summarize_t:
    """Proxy of C svn_client_diff_summarize_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_client_diff_summarize_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_client_diff_summarize_t, name)
    def __repr__(self):
        return "<%s.%s; proxy of C svn_client_diff_summarize_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["path"] = _client.svn_client_diff_summarize_t_path_set
    __swig_getmethods__["path"] = _client.svn_client_diff_summarize_t_path_get
    __swig_setmethods__["summarize_kind"] = _client.svn_client_diff_summarize_t_summarize_kind_set
    __swig_getmethods__["summarize_kind"] = _client.svn_client_diff_summarize_t_summarize_kind_get
    __swig_setmethods__["prop_changed"] = _client.svn_client_diff_summarize_t_prop_changed_set
    __swig_getmethods__["prop_changed"] = _client.svn_client_diff_summarize_t_prop_changed_get
    __swig_setmethods__["node_kind"] = _client.svn_client_diff_summarize_t_node_kind_set
    __swig_getmethods__["node_kind"] = _client.svn_client_diff_summarize_t_node_kind_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_client_diff_summarize_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)

    def __init__(self, *args):
        """__init__(self) -> svn_client_diff_summarize_t"""
        _swig_setattr(self, svn_client_diff_summarize_t, 'this', apply(_client.new_svn_client_diff_summarize_t, args))
        _swig_setattr(self, svn_client_diff_summarize_t, 'thisown', 1)
    def __del__(self, destroy=_client.delete_svn_client_diff_summarize_t):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class svn_client_diff_summarize_tPtr(svn_client_diff_summarize_t):
    def __init__(self, this):
        _swig_setattr(self, svn_client_diff_summarize_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_client_diff_summarize_t, 'thisown', 0)
        _swig_setattr(self, svn_client_diff_summarize_t,self.__class__,svn_client_diff_summarize_t)
_client.svn_client_diff_summarize_t_swigregister(svn_client_diff_summarize_tPtr)


def svn_client_diff_summarize_dup(*args):
    """svn_client_diff_summarize_dup(svn_client_diff_summarize_t diff, apr_pool_t pool) -> svn_client_diff_summarize_t"""
    return apply(_client.svn_client_diff_summarize_dup, args)
class svn_client_ctx_t:
    """Proxy of C svn_client_ctx_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_client_ctx_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_client_ctx_t, name)
    def __repr__(self):
        return "<%s.%s; proxy of C svn_client_ctx_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["auth_baton"] = _client.svn_client_ctx_t_auth_baton_set
    __swig_getmethods__["auth_baton"] = _client.svn_client_ctx_t_auth_baton_get
    __swig_setmethods__["notify_func"] = _client.svn_client_ctx_t_notify_func_set
    __swig_getmethods__["notify_func"] = _client.svn_client_ctx_t_notify_func_get
    __swig_setmethods__["notify_baton"] = _client.svn_client_ctx_t_notify_baton_set
    __swig_getmethods__["notify_baton"] = _client.svn_client_ctx_t_notify_baton_get
    __swig_setmethods__["log_msg_func"] = _client.svn_client_ctx_t_log_msg_func_set
    __swig_getmethods__["log_msg_func"] = _client.svn_client_ctx_t_log_msg_func_get
    __swig_setmethods__["log_msg_baton"] = _client.svn_client_ctx_t_log_msg_baton_set
    __swig_getmethods__["log_msg_baton"] = _client.svn_client_ctx_t_log_msg_baton_get
    __swig_setmethods__["config"] = _client.svn_client_ctx_t_config_set
    __swig_getmethods__["config"] = _client.svn_client_ctx_t_config_get
    __swig_setmethods__["cancel_func"] = _client.svn_client_ctx_t_cancel_func_set
    __swig_getmethods__["cancel_func"] = _client.svn_client_ctx_t_cancel_func_get
    __swig_setmethods__["cancel_baton"] = _client.svn_client_ctx_t_cancel_baton_set
    __swig_getmethods__["cancel_baton"] = _client.svn_client_ctx_t_cancel_baton_get
    __swig_setmethods__["notify_func2"] = _client.svn_client_ctx_t_notify_func2_set
    __swig_getmethods__["notify_func2"] = _client.svn_client_ctx_t_notify_func2_get
    __swig_setmethods__["notify_baton2"] = _client.svn_client_ctx_t_notify_baton2_set
    __swig_getmethods__["notify_baton2"] = _client.svn_client_ctx_t_notify_baton2_get
    __swig_setmethods__["log_msg_func2"] = _client.svn_client_ctx_t_log_msg_func2_set
    __swig_getmethods__["log_msg_func2"] = _client.svn_client_ctx_t_log_msg_func2_get
    __swig_setmethods__["log_msg_baton2"] = _client.svn_client_ctx_t_log_msg_baton2_set
    __swig_getmethods__["log_msg_baton2"] = _client.svn_client_ctx_t_log_msg_baton2_get
    __swig_setmethods__["progress_func"] = _client.svn_client_ctx_t_progress_func_set
    __swig_getmethods__["progress_func"] = _client.svn_client_ctx_t_progress_func_get
    __swig_setmethods__["progress_baton"] = _client.svn_client_ctx_t_progress_baton_set
    __swig_getmethods__["progress_baton"] = _client.svn_client_ctx_t_progress_baton_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_client_ctx_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)

    def __init__(self, *args):
        """__init__(self) -> svn_client_ctx_t"""
        _swig_setattr(self, svn_client_ctx_t, 'this', apply(_client.new_svn_client_ctx_t, args))
        _swig_setattr(self, svn_client_ctx_t, 'thisown', 1)
    def __del__(self, destroy=_client.delete_svn_client_ctx_t):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class svn_client_ctx_tPtr(svn_client_ctx_t):
    def __init__(self, this):
        _swig_setattr(self, svn_client_ctx_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_client_ctx_t, 'thisown', 0)
        _swig_setattr(self, svn_client_ctx_t,self.__class__,svn_client_ctx_t)
_client.svn_client_ctx_t_swigregister(svn_client_ctx_tPtr)

SVN_CLIENT_AUTH_USERNAME = _client.SVN_CLIENT_AUTH_USERNAME
SVN_CLIENT_AUTH_PASSWORD = _client.SVN_CLIENT_AUTH_PASSWORD

def svn_client_create_context(*args):
    """svn_client_create_context(svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t"""
    return apply(_client.svn_client_create_context, args)

def svn_client_checkout2(*args):
    """
    svn_client_checkout2(svn_revnum_t result_rev, char URL, char path, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_boolean_t ignore_externals, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_checkout2, args)

def svn_client_checkout(*args):
    """
    svn_client_checkout(svn_revnum_t result_rev, char URL, char path, svn_opt_revision_t revision, 
        svn_boolean_t recurse, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_checkout, args)

def svn_client_update2(*args):
    """
    svn_client_update2(apr_array_header_t result_revs, apr_array_header_t paths, 
        svn_opt_revision_t revision, svn_boolean_t recurse, 
        svn_boolean_t ignore_externals, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_update2, args)

def svn_client_update(*args):
    """
    svn_client_update(svn_revnum_t result_rev, char path, svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_update, args)

def svn_client_switch(*args):
    """
    svn_client_switch(svn_revnum_t result_rev, char path, char url, svn_opt_revision_t revision, 
        svn_boolean_t recurse, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_switch, args)

def svn_client_add3(*args):
    """
    svn_client_add3(char path, svn_boolean_t recursive, svn_boolean_t force, 
        svn_boolean_t no_ignore, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_add3, args)

def svn_client_add2(*args):
    """
    svn_client_add2(char path, svn_boolean_t recursive, svn_boolean_t force, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_add2, args)

def svn_client_add(*args):
    """
    svn_client_add(char path, svn_boolean_t recursive, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_add, args)

def svn_client_mkdir2(*args):
    """
    svn_client_mkdir2(svn_commit_info_t commit_info_p, apr_array_header_t paths, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_mkdir2, args)

def svn_client_mkdir(*args):
    """
    svn_client_mkdir(svn_client_commit_info_t commit_info_p, apr_array_header_t paths, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_mkdir, args)

def svn_client_delete2(*args):
    """
    svn_client_delete2(svn_commit_info_t commit_info_p, apr_array_header_t paths, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_delete2, args)

def svn_client_delete(*args):
    """
    svn_client_delete(svn_client_commit_info_t commit_info_p, apr_array_header_t paths, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_delete, args)

def svn_client_import2(*args):
    """
    svn_client_import2(svn_commit_info_t commit_info_p, char path, char url, 
        svn_boolean_t nonrecursive, svn_boolean_t no_ignore, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_import2, args)

def svn_client_import(*args):
    """
    svn_client_import(svn_client_commit_info_t commit_info_p, char path, 
        char url, svn_boolean_t nonrecursive, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_import, args)

def svn_client_commit3(*args):
    """
    svn_client_commit3(svn_commit_info_t commit_info_p, apr_array_header_t targets, 
        svn_boolean_t recurse, svn_boolean_t keep_locks, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_commit3, args)

def svn_client_commit2(*args):
    """
    svn_client_commit2(svn_client_commit_info_t commit_info_p, apr_array_header_t targets, 
        svn_boolean_t recurse, svn_boolean_t keep_locks, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_commit2, args)

def svn_client_commit(*args):
    """
    svn_client_commit(svn_client_commit_info_t commit_info_p, apr_array_header_t targets, 
        svn_boolean_t nonrecursive, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_commit, args)

def svn_client_status2(*args):
    """
    svn_client_status2(svn_revnum_t result_rev, char path, svn_opt_revision_t revision, 
        svn_wc_status_func2_t status_func, 
        void status_baton, svn_boolean_t recurse, 
        svn_boolean_t get_all, svn_boolean_t update, 
        svn_boolean_t no_ignore, svn_boolean_t ignore_externals, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_status2, args)

def svn_client_status(*args):
    """
    svn_client_status(svn_revnum_t result_rev, char path, svn_opt_revision_t revision, 
        svn_wc_status_func_t status_func, 
        svn_boolean_t recurse, svn_boolean_t get_all, 
        svn_boolean_t update, svn_boolean_t no_ignore, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_status, args)

def svn_client_log3(*args):
    """
    svn_client_log3(apr_array_header_t targets, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start, svn_opt_revision_t end, 
        int limit, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, 
        svn_log_message_receiver_t receiver, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_log3, args)

def svn_client_log2(*args):
    """
    svn_client_log2(apr_array_header_t targets, svn_opt_revision_t start, 
        svn_opt_revision_t end, int limit, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, 
        svn_log_message_receiver_t receiver, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_log2, args)

def svn_client_log(*args):
    """
    svn_client_log(apr_array_header_t targets, svn_opt_revision_t start, 
        svn_opt_revision_t end, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, 
        svn_log_message_receiver_t receiver, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_log, args)

def svn_client_blame3(*args):
    """
    svn_client_blame3(char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start, svn_opt_revision_t end, 
        svn_diff_file_options_t diff_options, svn_boolean_t ignore_mime_type, 
        svn_client_blame_receiver_t receiver, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_blame3, args)

def svn_client_blame2(*args):
    """
    svn_client_blame2(char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start, svn_opt_revision_t end, 
        svn_client_blame_receiver_t receiver, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_blame2, args)

def svn_client_blame(*args):
    """
    svn_client_blame(char path_or_url, svn_opt_revision_t start, svn_opt_revision_t end, 
        svn_client_blame_receiver_t receiver, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_blame, args)

def svn_client_diff3(*args):
    """
    svn_client_diff3(apr_array_header_t diff_options, char path1, svn_opt_revision_t revision1, 
        char path2, svn_opt_revision_t revision2, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, 
        svn_boolean_t ignore_content_type, 
        char header_encoding, apr_file_t outfile, 
        apr_file_t errfile, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_diff3, args)

def svn_client_diff2(*args):
    """
    svn_client_diff2(apr_array_header_t diff_options, char path1, svn_opt_revision_t revision1, 
        char path2, svn_opt_revision_t revision2, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, 
        svn_boolean_t ignore_content_type, 
        apr_file_t outfile, apr_file_t errfile, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_diff2, args)

def svn_client_diff(*args):
    """
    svn_client_diff(apr_array_header_t diff_options, char path1, svn_opt_revision_t revision1, 
        char path2, svn_opt_revision_t revision2, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, 
        apr_file_t outfile, apr_file_t errfile, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_diff, args)

def svn_client_diff_peg3(*args):
    """
    svn_client_diff_peg3(apr_array_header_t diff_options, char path, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start_revision, 
        svn_opt_revision_t end_revision, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, svn_boolean_t ignore_content_type, 
        char header_encoding, 
        apr_file_t outfile, apr_file_t errfile, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_diff_peg3, args)

def svn_client_diff_peg2(*args):
    """
    svn_client_diff_peg2(apr_array_header_t diff_options, char path, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start_revision, 
        svn_opt_revision_t end_revision, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, svn_boolean_t ignore_content_type, 
        apr_file_t outfile, 
        apr_file_t errfile, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_diff_peg2, args)

def svn_client_diff_peg(*args):
    """
    svn_client_diff_peg(apr_array_header_t diff_options, char path, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start_revision, 
        svn_opt_revision_t end_revision, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, apr_file_t outfile, 
        apr_file_t errfile, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_diff_peg, args)

def svn_client_diff_summarize(*args):
    """
    svn_client_diff_summarize(char path1, svn_opt_revision_t revision1, char path2, 
        svn_opt_revision_t revision2, svn_boolean_t recurse, 
        svn_boolean_t ignore_ancestry, svn_client_diff_summarize_func_t summarize_func, 
        void summarize_baton, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_diff_summarize, args)

def svn_client_diff_summarize_peg(*args):
    """
    svn_client_diff_summarize_peg(char path, svn_opt_revision_t peg_revision, svn_opt_revision_t start_revision, 
        svn_opt_revision_t end_revision, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_client_diff_summarize_func_t summarize_func, 
        void summarize_baton, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_diff_summarize_peg, args)

def svn_client_merge2(*args):
    """
    svn_client_merge2(char source1, svn_opt_revision_t revision1, char source2, 
        svn_opt_revision_t revision2, char target_wcpath, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t force, svn_boolean_t dry_run, 
        apr_array_header_t merge_options, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_merge2, args)

def svn_client_merge(*args):
    """
    svn_client_merge(char source1, svn_opt_revision_t revision1, char source2, 
        svn_opt_revision_t revision2, char target_wcpath, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t force, svn_boolean_t dry_run, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_merge, args)

def svn_client_merge_peg2(*args):
    """
    svn_client_merge_peg2(char source, svn_opt_revision_t revision1, svn_opt_revision_t revision2, 
        svn_opt_revision_t peg_revision, 
        char target_wcpath, svn_boolean_t recurse, 
        svn_boolean_t ignore_ancestry, svn_boolean_t force, 
        svn_boolean_t dry_run, apr_array_header_t merge_options, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_merge_peg2, args)

def svn_client_merge_peg(*args):
    """
    svn_client_merge_peg(char source, svn_opt_revision_t revision1, svn_opt_revision_t revision2, 
        svn_opt_revision_t peg_revision, 
        char target_wcpath, svn_boolean_t recurse, 
        svn_boolean_t ignore_ancestry, svn_boolean_t force, 
        svn_boolean_t dry_run, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_merge_peg, args)

def svn_client_cleanup(*args):
    """svn_client_cleanup(char dir, svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t"""
    return apply(_client.svn_client_cleanup, args)

def svn_client_relocate(*args):
    """
    svn_client_relocate(char dir, char from, char to, svn_boolean_t recurse, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_relocate, args)

def svn_client_revert(*args):
    """
    svn_client_revert(apr_array_header_t paths, svn_boolean_t recursive, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_revert, args)

def svn_client_resolved(*args):
    """
    svn_client_resolved(char path, svn_boolean_t recursive, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_resolved, args)

def svn_client_copy3(*args):
    """
    svn_client_copy3(svn_commit_info_t commit_info_p, char src_path, svn_opt_revision_t src_revision, 
        char dst_path, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_copy3, args)

def svn_client_copy2(*args):
    """
    svn_client_copy2(svn_commit_info_t commit_info_p, char src_path, svn_opt_revision_t src_revision, 
        char dst_path, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_copy2, args)

def svn_client_copy(*args):
    """
    svn_client_copy(svn_client_commit_info_t commit_info_p, char src_path, 
        svn_opt_revision_t src_revision, char dst_path, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_copy, args)

def svn_client_move4(*args):
    """
    svn_client_move4(svn_commit_info_t commit_info_p, char src_path, char dst_path, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_move4, args)

def svn_client_move3(*args):
    """
    svn_client_move3(svn_commit_info_t commit_info_p, char src_path, char dst_path, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_move3, args)

def svn_client_move2(*args):
    """
    svn_client_move2(svn_client_commit_info_t commit_info_p, char src_path, 
        char dst_path, svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_move2, args)

def svn_client_move(*args):
    """
    svn_client_move(svn_client_commit_info_t commit_info_p, char src_path, 
        svn_opt_revision_t src_revision, char dst_path, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_move, args)

def svn_client_propset2(*args):
    """
    svn_client_propset2(char propname, svn_string_t propval, char target, svn_boolean_t recurse, 
        svn_boolean_t skip_checks, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_propset2, args)

def svn_client_propset(*args):
    """
    svn_client_propset(char propname, svn_string_t propval, char target, svn_boolean_t recurse, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_propset, args)

def svn_client_revprop_set(*args):
    """
    svn_client_revprop_set(char propname, svn_string_t propval, char URL, svn_opt_revision_t revision, 
        svn_revnum_t set_rev, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_revprop_set, args)

def svn_client_propget2(*args):
    """
    svn_client_propget2(apr_hash_t props, char propname, char target, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_propget2, args)

def svn_client_propget(*args):
    """
    svn_client_propget(apr_hash_t props, char propname, char target, svn_opt_revision_t revision, 
        svn_boolean_t recurse, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_propget, args)

def svn_client_revprop_get(*args):
    """
    svn_client_revprop_get(char propname, svn_string_t propval, char URL, svn_opt_revision_t revision, 
        svn_revnum_t set_rev, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_revprop_get, args)

def svn_client_proplist2(*args):
    """
    svn_client_proplist2(apr_array_header_t props, char target, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_proplist2, args)

def svn_client_proplist(*args):
    """
    svn_client_proplist(apr_array_header_t props, char target, svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_proplist, args)

def svn_client_revprop_list(*args):
    """
    svn_client_revprop_list(apr_hash_t props, char URL, svn_opt_revision_t revision, 
        svn_revnum_t set_rev, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_revprop_list, args)

def svn_client_export3(*args):
    """
    svn_client_export3(svn_revnum_t result_rev, char from, char to, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_boolean_t overwrite, svn_boolean_t ignore_externals, 
        svn_boolean_t recurse, 
        char native_eol, svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_export3, args)

def svn_client_export2(*args):
    """
    svn_client_export2(svn_revnum_t result_rev, char from, char to, svn_opt_revision_t revision, 
        svn_boolean_t force, char native_eol, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_export2, args)

def svn_client_export(*args):
    """
    svn_client_export(svn_revnum_t result_rev, char from, char to, svn_opt_revision_t revision, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_export, args)

def svn_client_list(*args):
    """
    svn_client_list(char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, svn_boolean_t recurse, 
        apr_uint32_t dirent_fields, svn_boolean_t fetch_locks, 
        svn_client_list_func_t list_func, 
        void baton, svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_list, args)

def svn_client_ls3(*args):
    """
    svn_client_ls3(apr_hash_t dirents, apr_hash_t locks, char path_or_url, 
        svn_opt_revision_t peg_revision, svn_opt_revision_t revision, 
        svn_boolean_t recurse, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_ls3, args)

def svn_client_ls2(*args):
    """
    svn_client_ls2(apr_hash_t dirents, char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_ls2, args)

def svn_client_ls(*args):
    """
    svn_client_ls(apr_hash_t dirents, char path_or_url, svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_ls, args)

def svn_client_cat2(*args):
    """
    svn_client_cat2(svn_stream_t out, char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_cat2, args)

def svn_client_cat(*args):
    """
    svn_client_cat(svn_stream_t out, char path_or_url, svn_opt_revision_t revision, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_cat, args)

def svn_client_lock(*args):
    """
    svn_client_lock(apr_array_header_t targets, char comment, svn_boolean_t steal_lock, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_lock, args)

def svn_client_unlock(*args):
    """
    svn_client_unlock(apr_array_header_t targets, svn_boolean_t break_lock, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_unlock, args)
class svn_info_t:
    """Proxy of C svn_info_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_info_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_info_t, name)
    def __repr__(self):
        return "<%s.%s; proxy of C svn_info_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["URL"] = _client.svn_info_t_URL_set
    __swig_getmethods__["URL"] = _client.svn_info_t_URL_get
    __swig_setmethods__["rev"] = _client.svn_info_t_rev_set
    __swig_getmethods__["rev"] = _client.svn_info_t_rev_get
    __swig_setmethods__["kind"] = _client.svn_info_t_kind_set
    __swig_getmethods__["kind"] = _client.svn_info_t_kind_get
    __swig_setmethods__["repos_root_URL"] = _client.svn_info_t_repos_root_URL_set
    __swig_getmethods__["repos_root_URL"] = _client.svn_info_t_repos_root_URL_get
    __swig_setmethods__["repos_UUID"] = _client.svn_info_t_repos_UUID_set
    __swig_getmethods__["repos_UUID"] = _client.svn_info_t_repos_UUID_get
    __swig_setmethods__["last_changed_rev"] = _client.svn_info_t_last_changed_rev_set
    __swig_getmethods__["last_changed_rev"] = _client.svn_info_t_last_changed_rev_get
    __swig_setmethods__["last_changed_date"] = _client.svn_info_t_last_changed_date_set
    __swig_getmethods__["last_changed_date"] = _client.svn_info_t_last_changed_date_get
    __swig_setmethods__["last_changed_author"] = _client.svn_info_t_last_changed_author_set
    __swig_getmethods__["last_changed_author"] = _client.svn_info_t_last_changed_author_get
    __swig_setmethods__["lock"] = _client.svn_info_t_lock_set
    __swig_getmethods__["lock"] = _client.svn_info_t_lock_get
    __swig_setmethods__["has_wc_info"] = _client.svn_info_t_has_wc_info_set
    __swig_getmethods__["has_wc_info"] = _client.svn_info_t_has_wc_info_get
    __swig_setmethods__["schedule"] = _client.svn_info_t_schedule_set
    __swig_getmethods__["schedule"] = _client.svn_info_t_schedule_get
    __swig_setmethods__["copyfrom_url"] = _client.svn_info_t_copyfrom_url_set
    __swig_getmethods__["copyfrom_url"] = _client.svn_info_t_copyfrom_url_get
    __swig_setmethods__["copyfrom_rev"] = _client.svn_info_t_copyfrom_rev_set
    __swig_getmethods__["copyfrom_rev"] = _client.svn_info_t_copyfrom_rev_get
    __swig_setmethods__["text_time"] = _client.svn_info_t_text_time_set
    __swig_getmethods__["text_time"] = _client.svn_info_t_text_time_get
    __swig_setmethods__["prop_time"] = _client.svn_info_t_prop_time_set
    __swig_getmethods__["prop_time"] = _client.svn_info_t_prop_time_get
    __swig_setmethods__["checksum"] = _client.svn_info_t_checksum_set
    __swig_getmethods__["checksum"] = _client.svn_info_t_checksum_get
    __swig_setmethods__["conflict_old"] = _client.svn_info_t_conflict_old_set
    __swig_getmethods__["conflict_old"] = _client.svn_info_t_conflict_old_get
    __swig_setmethods__["conflict_new"] = _client.svn_info_t_conflict_new_set
    __swig_getmethods__["conflict_new"] = _client.svn_info_t_conflict_new_get
    __swig_setmethods__["conflict_wrk"] = _client.svn_info_t_conflict_wrk_set
    __swig_getmethods__["conflict_wrk"] = _client.svn_info_t_conflict_wrk_get
    __swig_setmethods__["prejfile"] = _client.svn_info_t_prejfile_set
    __swig_getmethods__["prejfile"] = _client.svn_info_t_prejfile_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_info_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)

    def __init__(self, *args):
        """__init__(self) -> svn_info_t"""
        _swig_setattr(self, svn_info_t, 'this', apply(_client.new_svn_info_t, args))
        _swig_setattr(self, svn_info_t, 'thisown', 1)
    def __del__(self, destroy=_client.delete_svn_info_t):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class svn_info_tPtr(svn_info_t):
    def __init__(self, this):
        _swig_setattr(self, svn_info_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_info_t, 'thisown', 0)
        _swig_setattr(self, svn_info_t,self.__class__,svn_info_t)
_client.svn_info_t_swigregister(svn_info_tPtr)


def svn_info_dup(*args):
    """svn_info_dup(svn_info_t info, apr_pool_t pool) -> svn_info_t"""
    return apply(_client.svn_info_dup, args)

def svn_client_info(*args):
    """
    svn_client_info(char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, svn_info_receiver_t receiver, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_info, args)

def svn_client_url_from_path(*args):
    """svn_client_url_from_path(char url, char path_or_url, apr_pool_t pool) -> svn_error_t"""
    return apply(_client.svn_client_url_from_path, args)

def svn_client_uuid_from_url(*args):
    """svn_client_uuid_from_url(char uuid, char url, svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t"""
    return apply(_client.svn_client_uuid_from_url, args)

def svn_client_uuid_from_path(*args):
    """
    svn_client_uuid_from_path(char uuid, char path, svn_wc_adm_access_t adm_access, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_uuid_from_path, args)

def svn_client_open_ra_session(*args):
    """
    svn_client_open_ra_session(svn_ra_session_t session, char url, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_client.svn_client_open_ra_session, args)

