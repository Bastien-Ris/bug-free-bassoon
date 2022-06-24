"######################################
"#_   _         __     ___            #
"#| \ | | ___  __\ \   / (_)_ __ ___  #
"#|  \| |/ _ \/ _ \ \ / /| | '_ ` _ \ #
"#| |\  |  __/ (_) \ V / | | | | | | |#
"#|_| \_|\___|\___/ \_/  |_|_| |_| |_|#
"######################################                                   

"stand 21.06.22 BR


set nocompatible            " disable compatibility to old-time vi

"set showmatch               " show matching 

"set mouse=v                 " middle-click paste with 
"set mouse=a                 " enable mouse click

set ignorecase              " case insensitive 


set hlsearch                " highlight search 
set incsearch               " incremental search
set tabstop=4               " number of columns occupied by a tab 
set softtabstop=4           " see multiple spaces as tabstops so <BS> does the right thing
set expandtab               " converts tabs to white space
set shiftwidth=4            " width for autoindents
set autoindent              " indent a new line the same amount as the line just typed
set number                  " add line numbers
set wildmode=longest,list   " get bash-like tab completions
set cc=80                  " set an 80 column border for good coding style
filetype plugin indent on   "allow auto-indenting depending on file type
syntax on                   " syntax highlighting
set clipboard=unnamedplus   " using system clipboard
filetype plugin on
set cursorline              " highlight current cursorline
set ttyfast                 " Speed up scrolling in Vim
set spell                 " enable spell check (may need to download language package)
set noswapfile            " disable creating swap file
"set backupdir=~/.cache/vim " Directory to store backup files.

"##############################################################################
"#                               Plugins
"############################################################################## 

call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')


if has('nvim')
  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif
let g:deoplete#enable_at_startup = 1
"Plug 'Shougo/deoplete'                        " completion

Plug 'dpelle/vim-LanguageTool'

Plug 'vifm/vifm.vim'

"dev and ed environment
Plug 'vim-python/python-syntax'                     " Python highlighting
Plug 'tbastos/vim-lua'                              " Lua highlighting    
Plug 'ap/vim-css-color'                             " Color preview CSS
Plug 'lervag/vimtex'                                 " Tex editor
Plug 'othree/xml.vim'
Plug 'vim-pandoc/vim-pandoc'
Plug 'vim-pandoc/vim-pandoc-syntax' 
Plug 'frazrepo/vim-rainbow'                         " diversify highlighting color for readability    
Plug 'jiangmiao/auto-pairs'                         "autopair characters lis (), etc
" Using plug

Plug 'dylanaraps/wal.vim'
Plug 'itchyny/lightline.vim'

" List ends here. Plugins become visible to Vim after this call.
call plug#end()

let g:vimtex_view_method = 'zathura'

"###############################################################################
"#                               Colors
"###############################################################################

colorscheme wal

let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ }

"#################################################################
"## aliases
"##################################################################

map <Leader>vv :Vifm<CR>
map <Leader>vs :VsplitVifm<CR>
map <Leader>sp :SplitVifm<CR>
map <Leader>dv :DiffVifm<CR>
map <Leader>tv :TabVifm<CR>
