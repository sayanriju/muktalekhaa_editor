#!/usr/bin/env python
# coding: utf-8
## beditor.py

###############################################################################################
##		Copyright 2007 Sayan "Riju" Chakrabarti <sayan.marchlinux@gmail.com>
##
##		This file is part of Muktalekhaa : A Bangla Phonetic Text Editor for GNU/Linux Systems
##
##      Muktalekhaa is FREE software; you can redistribute it and/or modify
##      it under the terms of the GNU General Public License as published by
##      the Free Software Foundation; either version 3 of the License, or
##      (at your option) any later version.
##       
##      This program is distributed in the hope that it will be useful,
##      but WITHOUT ANY WARRANTY; without even the implied warranty of
##      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##      GNU General Public License for more details.
##       
##      You should have received a copy of the GNU General Public License
##      along with Muktalekhaa. If not, see <http://www.gnu.org/licenses/>.
###############################################################################################



''' Beditor : The GUI editor part of Muktalekhaa '''

import wx
import os
import engine

window_title = 'Muktalekhaa' + '   ->   '

class Beditor(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(600,400))

		# variables
		self.modify = False
		self.last_name_saved = ''
		self.replace = False

		# setting up menubar
		menubar = wx.MenuBar()

		file = wx.Menu()
		new = wx.MenuItem(file, 101, '&New\tCtrl+N', 'Creates a new document')
		new.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/stock_new-16.png'))
		file.AppendItem(new)

		open = wx.MenuItem(file, 102, '&Open\tCtrl+O', 'Open an existing file')
		open.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/stock_open-16.png'))
		file.AppendItem(open)
		file.AppendSeparator()

		save = wx.MenuItem(file, 103, '&Save\tCtrl+S', 'Save the file')
		save.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/stock_save-16.png'))
		file.AppendItem(save)

		saveas = wx.MenuItem(file, 104, 'Save &As...\tShift+Ctrl+S', 'Save the file with a different name')
		saveas.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/stock_save_as-16.png'))
		file.AppendItem(saveas)
		file.AppendSeparator()

		quit = wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')
		quit.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/stock_exit-16.png'))
		file.AppendItem(quit)

		edit = wx.Menu()
		cut = wx.MenuItem(edit, 106, '&Cut\tCtrl+X', 'Cut the Selection')
		cut.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/stock_cut-16.png'))
		edit.AppendItem(cut)

		copy = wx.MenuItem(edit, 107, '&Copy\tCtrl+C', 'Copy the Selection')
		copy.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/stock_copy-16.png'))
		edit.AppendItem(copy)

		paste = wx.MenuItem(edit, 108, '&Paste\tCtrl+V', 'Paste text from clipboard')
		paste.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/stock_paste-16.png'))
		edit.AppendItem(paste)

		delete = wx.MenuItem(edit, 109, '&Delete', 'Delete the selected text')
		delete.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/stock_delete-16.png',))

		edit.AppendItem(delete)
		edit.AppendSeparator()
		edit.Append(110, 'Select &All\tCtrl+A', 'Select the entire text')

		view = wx.Menu()
		view.Append(111, '&Statusbar', 'Hide/Show StatusBar')
		view.Append(503, '&Toolbar', 'Hide/Show ToolBar')
		
		
		view.AppendSeparator()
		
		fontsel = wx.MenuItem(view, 501, '&Select Font', 'Select Font to use in the current document')
		fontsel.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/fontsel.png'))
		view.AppendItem(fontsel)


		help = wx.Menu()
		about = wx.MenuItem(help, 112, '&About', 'About Editor')
		about.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/stock_about-16.png'))
		help.AppendItem(about)
		
		layout_help = wx.MenuItem(help, 502, '&Layout Help\tF1', 'Get Help on Key Layout')
		layout_help.SetBitmap(wx.Bitmap('/usr/share/muktalekhaa/icons/help-16.png'))
		help.AppendItem(layout_help)		


		menubar.Append(file, '&File')
		menubar.Append(edit, '&Edit')
		menubar.Append(view, '&View')
		menubar.Append(help, '&Help')
		self.SetMenuBar(menubar)

		self.Bind(wx.EVT_MENU, self.NewApplication, id=101)
		self.Bind(wx.EVT_MENU, self.OnOpenFile, id=102)
		self.Bind(wx.EVT_MENU, self.OnSaveFile, id=103)
		self.Bind(wx.EVT_MENU, self.OnSaveAsFile, id=104)
		self.Bind(wx.EVT_MENU, self.QuitApplication, id=105)
		self.Bind(wx.EVT_MENU, self.OnCut, id=106)
		self.Bind(wx.EVT_MENU, self.OnCopy, id=107)
		self.Bind(wx.EVT_MENU, self.OnPaste, id=108)
		self.Bind(wx.EVT_MENU, self.OnDelete, id=109)
		self.Bind(wx.EVT_MENU, self.OnSelectAll, id=110)
		self.Bind(wx.EVT_MENU, self.ToggleStatusBar, id=111)
		self.Bind(wx.EVT_MENU, self.OnAbout, id=112)
		self.Bind(wx.EVT_MENU, self.FontSel, id=501)
		self.Bind(wx.EVT_MENU, self.LayoutHelp, id=502)
		self.Bind(wx.EVT_MENU, self.ToggleToolbar, id=503)
		
		# setting up toolbar
		self.toolbar = self.CreateToolBar( wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT )
		self.toolbar.AddSimpleTool(801, wx.Bitmap('/usr/share/muktalekhaa/icons/document-new.png'), 'New', '')
		self.toolbar.AddSimpleTool(802, wx.Bitmap('/usr/share/muktalekhaa/icons/document-open.png'), 'Open', '')
		self.toolbar.AddSimpleTool(803, wx.Bitmap('/usr/share/muktalekhaa/icons/document-save.png'), 'Save', '')
		self.toolbar.AddSeparator()

		self.toolbar.AddSimpleTool(804, wx.Bitmap('/usr/share/muktalekhaa/icons/edit-cut.png'), 'Cut', '')
		self.toolbar.AddSimpleTool(805, wx.Bitmap('/usr/share/muktalekhaa/icons/edit-copy.png'), 'Copy', '')
		self.toolbar.AddSimpleTool(806, wx.Bitmap('/usr/share/muktalekhaa/icons/edit-paste.png'), 'Paste', '')
		self.toolbar.AddSeparator()

		self.toolbar.AddSimpleTool(501, wx.Bitmap('/usr/share/muktalekhaa/icons/fontsel-22.png'), 'Select Font', '')
		self.toolbar.AddSimpleTool(502, wx.Bitmap('/usr/share/muktalekhaa/icons/help.png'), 'Layout Help', '')
		
		self.toolbar.AddSeparator()
		
		self.toolbar.AddSimpleTool(807, wx.Bitmap('/usr/share/muktalekhaa/icons/process-stop.png'), 'Exit', '')
		
		self.toolbar.Realize()

		self.Bind(wx.EVT_TOOL, self.NewApplication, id=801)
		self.Bind(wx.EVT_TOOL, self.OnOpenFile, id=802)
		self.Bind(wx.EVT_TOOL, self.OnSaveFile, id=803)
		self.Bind(wx.EVT_TOOL, self.OnCut, id=804)
		self.Bind(wx.EVT_TOOL, self.OnCopy, id=805)
		self.Bind(wx.EVT_TOOL, self.OnPaste, id=806)
		self.Bind(wx.EVT_TOOL, self.QuitApplication, id=807)

		self.text = wx.TextCtrl(self, 1000, '', size=(-1, -1), style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER)
		self.text.SetFocus()
		self.text.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		self.text.Bind(wx.EVT_TEXT, self.OnTextChanged, id=1000)
		self.text.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
		self.text.Bind(wx.EVT_CHAR, self.conv)
		

		self.Bind(wx.EVT_CLOSE, self.QuitApplication)

		self.StatusBar()

		self.Centre()
		self.Show(True)

	def NewApplication(self, event):
		editor = Beditor(None, -1, window_title + '[Untitled]'  )
		editor.Centre()
		editor.Show()

	def OnOpenFile(self, event):
		file_name = os.path.basename(self.last_name_saved)
		if self.modify:
			dlg = wx.MessageDialog(self, 'Save changes?', '', wx.YES_NO | wx.YES_DEFAULT | wx.CANCEL |
						wx.ICON_QUESTION)
			val = dlg.ShowModal()
			if val == wx.ID_YES:
				self.OnSaveFile(event)
				self.DoOpenFile()
			elif val == wx.ID_CANCEL:
				dlg.Destroy()
			else:
				self.DoOpenFile()
		else:
			self.DoOpenFile()

	def DoOpenFile(self):
		wcd = 'All files (*)|*|Editor files (*.ef)|*.ef|'
		dir = os.getcwd()
		open_dlg = wx.FileDialog(self, message='Choose a file', defaultDir=dir, defaultFile='',
						wildcard=wcd, style=wx.OPEN|wx.CHANGE_DIR)
		if open_dlg.ShowModal() == wx.ID_OK:
			path = open_dlg.GetPath()

			try:
				file = open(path, 'r')
				text = file.read()
				file.close()
				if self.text.GetLastPosition():
					self.text.Clear()
				self.text.WriteText(text)
				self.last_name_saved = path
				self.statusbar.SetStatusText('', 1)
				self.modify = False
				self.SetTitle(window_title + path)

			except IOError, error:
				dlg = wx.MessageDialog(self, 'Error opening file\n' + str(error))
				dlg.ShowModal()

			except UnicodeDecodeError, error:
				dlg = wx.MessageDialog(self, 'Error opening file\n' + str(error))
				dlg.ShowModal()

		open_dlg.Destroy()
	def OnSaveFile(self, event):
		if self.last_name_saved:

			try:
				file = open(self.last_name_saved, 'w')
				text = self.text.GetValue()
				file.write(text.encode('utf-8'))
				file.close()
				self.statusbar.SetStatusText(os.path.basename(self.last_name_saved) + ' saved', 0)
				self.modify = False
				self.statusbar.SetStatusText('', 1)

			except IOError, error:
				dlg = wx.MessageDialog(self, 'Error saving file\n' + str(error))
				dlg.ShowModal()
		else:
			self.OnSaveAsFile(event)

	def OnSaveAsFile(self, event):
		wcd='All files(*)|*|Editor files (*.ef)|*.ef|'
		dir = os.getcwd()
		save_dlg = wx.FileDialog(self, message='Save file as...', defaultDir=dir, defaultFile='',
						wildcard=wcd, style=wx.SAVE | wx.OVERWRITE_PROMPT)
		if save_dlg.ShowModal() == wx.ID_OK:
			path = save_dlg.GetPath()

			try:
				file = open(path, 'w')
				text = self.text.GetValue()
				file.write(text.encode('utf-8'))
				file.close()
				self.last_name_saved = os.path.basename(path)
				self.statusbar.SetStatusText(self.last_name_saved + ' saved', 0)
				self.modify = False
				self.statusbar.SetStatusText('', 1)
				self.SetTitle(window_title + path)
			except IOError, error:
				dlg = wx.MessageDialog(self, 'Error saving file\n' + str(error))
				dlg.ShowModal()
		save_dlg.Destroy()

	def OnCut(self, event):
		self.text.Cut()

	def OnCopy(self, event):
		self.text.Copy()

	def OnPaste(self, event):
		self.text.Paste()

	def QuitApplication(self, event):
		if self.modify:
			dlg = wx.MessageDialog(self, 'Save before Exit?', '', wx.YES_NO | wx.YES_DEFAULT |
						wx.CANCEL | wx.ICON_QUESTION)
			val = dlg.ShowModal()
			if val == wx.ID_YES:
				self.OnSaveFile(event)
				if not self.modify:
					wx.Exit()
			elif val == wx.ID_CANCEL:
				dlg.Destroy()
			else:
				self.Destroy()
		else:
			self.Destroy()

	def OnDelete(self, event):
		frm, to = self.text.GetSelection()
		self.text.Remove(frm, to)

	def OnSelectAll(self, event):
		self.text.SelectAll()

	def OnTextChanged(self, event):
		self.modify = True
		self.statusbar.SetStatusText(' modified', 1)
		event.Skip()

	def OnKeyDown(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_INSERT:
			if not self.replace:
				self.statusbar.SetStatusText('INS', 2)
				self.replace = True
			else:
				self.statusbar.SetStatusText('', 2)
				self.replace = False
		event.Skip()

	def ToggleStatusBar(self, event):
		if self.statusbar.IsShown():
			self.statusbar.Hide()
		else:
			self.statusbar.Show()
			
	def ToggleToolbar(self, event):
		if self.toolbar.IsShown():
			self.toolbar.Hide()
		else:
			self.toolbar.Show()

	def StatusBar(self):
		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetFieldsCount(3)
		self.statusbar.SetStatusWidths([-13, -3, -2])
		
	def LayoutHelp(self, event):
		info = wx.AboutDialogInfo()

		info.SetIcon(wx.Icon('/usr/share/muktalekhaa/icons/muktolekha.png', wx.BITMAP_TYPE_PNG))
		info.SetName('Layout')
		wx.AboutBox(info)


	def OnAbout(self, event):

		description = """গনুহ/লিনাক্সে ফোনেটিক বাংলা লেখার মুক্ত সফটওয়ার  """ """\n A Bangla Phonetic Text Editor for GNU/Linux systems\n"""

		licence = """ 
		Muktalekhaa is FREE software; you can redistribute it and/or modify it
		under the terms of the GNU General Public License as published by the Free Software Foundation; 
		either version 3 of the License, or (at your option) any later version.
		
		Muktalekhaa is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
		without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
		See the GNU General Public License for more details. You should have received a copy of 
		the GNU General Public License along with Muktalekhaa; if not, write to 
		the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  0211"""

		info = wx.AboutDialogInfo()
		
		info.SetIcon(wx.Icon('/usr/share/muktalekhaa/icons/logo.png', wx.BITMAP_TYPE_PNG))
		info.SetName('Muktalekhaa ')
		info.SetVersion('1.0')
		info.SetDescription(description)
		info.SetCopyright('(C) 2007 Sayan \"Riju\" Chakrabarti <sayan.marchlinux@gmail.com>')
		info.SetWebSite('http://code.google.com/p/muktalekhaa/')
		info.SetLicence(licence)
		info.AddDeveloper('Sayan \"Riju\" Chakrabarti')
		info.AddDocWriter('Shamik Ghosh')
		info.AddArtist('The Tango crew :-)')
				
		info.SetName('Muktalekhaa')
		wx.AboutBox(info)
		
		
	
	def FontSel(self, event):
		default_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "")
		data = wx.FontData()
		
		data.SetAllowSymbols(False)
		data.SetInitialFont(default_font)
		data.SetRange(10, 30)
		dlg = wx.FontDialog(self, data)
		if dlg.ShowModal() == wx.ID_OK:
			data = dlg.GetFontData()
			font = data.GetChosenFont()
			color = data.GetColour()
			text = 'Face: %s, Size: %d, Color: %s' % (font.GetFaceName(), font.GetPointSize(),  color.Get())
			self.text.SetFont(font)
		dlg.Destroy()
	
	###### converting to bangla using engine  ##########
	def conv(self, event):
		## New Algorithm for Ver 1.1
		keycode = event.GetKeyCode()
				
		if keycode == wx.WXK_SPACE:
			cur_word = self.text.GetRange(0, self.text.GetInsertionPoint())  ## cur_word  = current word
			self.text.Replace(0, self.text.GetInsertionPoint(), engine.roman2beng(cur_word.encode('utf-8')+' '))		
		else:
			event.Skip()
					
		


app = wx.App()
Beditor(None, -1, window_title + '[Untitled]')
app.MainLoop()
