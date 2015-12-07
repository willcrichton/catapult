# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
import uuid

class TraceHandle(object):
  # TODO(nduca): Extract metadata from trace instead of passing here.
  def __init__(self, url, display_name, metadata):
    self._url = url
    self._display_name = display_name
    self._metadata = metadata
    self._guid = uuid.uuid4()

  @property
  def url(self):
      return self._url

  @property
  def display_name(self):
      return self._display_name

  @property
  def metadata(self):
      return self._metadata

  @property
  def guid(self):
      return self._guid

  def Open(self):
    # Returns a with-able object containing a name.
    raise NotImplementedError()
