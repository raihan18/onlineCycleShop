 Code
 Revisions 2
 Stars 2
 Forks 5
Embed URL
	
HTTPS clone URL
	
You can clone with HTTPS or SSH.

 Download Gist
bootstrap-popover.js v2.0.1
 bootstrap-popover.js Raw
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
/* ===========================================================
 * bootstrap-popover.js v2.0.1
 * http://twitter.github.com/bootstrap/javascript.html#popovers
 * ===========================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * 
 * Modified 2012-02-28 by @danmillar to allow for maintained visibility
 * while the mouse is over the popover itself (rather than disappearing
 * when the mouse leaves the trigger). Note: Set a 'delay.hide' option.
 * https://gist.github.com/1930277
 * =========================================================== */
 
 
!function( $ ) {
 
 "use strict"
 
  var Popover = function ( element, options ) {
    this.init('popover', element, options);
  }
 
  /* NOTE: POPOVER EXTENDS BOOTSTRAP-TOOLTIP.js
     ========================================== */
 
  Popover.prototype = $.extend({}, $.fn.tooltip.Constructor.prototype, {
 
    constructor: Popover
 
  , setContent: function () {
      var $tip = this.tip()
        , title = this.getTitle()
        , content = this.getContent()
 
      $tip.find('.popover-title')[ $.type(title) == 'object' ? 'append' : 'html' ](title)
      $tip.find('.popover-content > *')[ $.type(content) == 'object' ? 'append' : 'html' ](content)
 
      $tip.removeClass('fade top bottom left right in')
    }
 
  , hasContent: function () {
      return this.getTitle() || this.getContent()
    }
 
  , getContent: function () {
      var content
        , $e = this.$element
        , o = this.options
 
      content = $e.attr('data-content')
        || (typeof o.content == 'function' ? o.content.call($e[0]) :  o.content)
 
      content = content.toString().replace(/(^\s*|\s*$)/, "")
 
      return content
    }
 
  , tip: function() {
      if (!this.$tip) {
        this.$tip = $(this.options.template)
      }
      return this.$tip
    }
 
  , show: function () {
      var $tip
        , inside
        , pos
        , actualWidth
        , actualHeight
        , placement
        , tp
 
      if (this.hasContent() && this.enabled) {
        $tip = this.tip()
        this.setContent()
 
        if (this.options.animation) {
          $tip.addClass('fade')
        }
 
        placement = typeof this.options.placement == 'function' ?
          this.options.placement.call(this, $tip[0], this.$element[0]) :
          this.options.placement
 
        inside = /in/.test(placement)
 
        $tip
          .remove()
          .css({ top: 0, left: 0, display: 'block' })
          .appendTo(inside ? this.$element : document.body)
 
        pos = this.getPosition(inside)
 
        actualWidth = $tip[0].offsetWidth
        actualHeight = $tip[0].offsetHeight
 
        switch (inside ? placement.split(' ')[1] : placement) {
          case 'bottom':
            tp = {top: pos.top + pos.height, left: pos.left + pos.width / 2 - actualWidth / 2}
            break
          case 'top':
            tp = {top: pos.top - actualHeight, left: pos.left + pos.width / 2 - actualWidth / 2}
            break
          case 'left':
            tp = {top: pos.top + pos.height / 2 - actualHeight / 2, left: pos.left - actualWidth}
            break
          case 'right':
            tp = {top: pos.top + pos.height / 2 - actualHeight / 2, left: pos.left + pos.width}
            break
        }
 
        $tip
          .css(tp)
          .addClass(placement)
          .addClass('in')
          .on('mouseenter', $.proxy(this.over, this))
          .on('mouseleave', $.proxy(this.out, this))
      }
    }
        
  , over: function( e ) {
      var self = $(this.$element)[this.type](this._options).data(this.type)
 
      self.hoverState = 'in'
    }
 
  , out: function( e ) {
      var self = $(this.$element)[this.type](this._options).data(this.type)
 
      if (!self.options.delay || !self.options.delay.hide) {
        self.hide()
      } else {
        self.hoverState = 'out'
        setTimeout(function() {
          if (self.hoverState == 'out') {
            self.hide()
          }
        }, self.options.delay.hide)
      }
    }
 
  })
 
 
 /* POPOVER PLUGIN DEFINITION
  * ======================= */
 
  $.fn.popover = function ( option ) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('popover')
        , options = typeof option == 'object' && option
      if (!data) $this.data('popover', (data = new Popover(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }
 
  $.fn.popover.Constructor = Popover
 
  $.fn.popover.defaults = $.extend({} , $.fn.tooltip.defaults, {
    placement: 'right'
  , content: ''
  , template: '<div class="popover"><div class="arrow"></div><div class="popover-inner"><h3 class="popover-title"></h3><div class="popover-content"><p></p></div></div></div>'
  })
 
}( window.jQuery );