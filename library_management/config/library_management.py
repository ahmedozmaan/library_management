from __future__ import unicode_literals
from frappe import _


def get_data():
	return [
		{
			"label": _("Library Management"),
			"icon": "octicon octicon-briefcase",
			"items": [
				{
					"type": "doctype",
					"name": "Library Member",
					"label": _("Library Member"),
					"description": _("Library Members List and Creation."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Library Membership",
					"label": _("Library Membership"),
					"description": _("Library Membership For Members Start and End date or if they pay."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Library Transaction",
					"label": _("Library Transaction"),
					"description": _("Library Transaction for isue and return Articles."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Sample Article",
					"label": _("Sample Article"),
					"description": _("Sample Article that you can issue for members."),
					"onboard": 1,
				}
			]
		}
	]