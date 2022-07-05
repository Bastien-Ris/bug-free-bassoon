 ;; Define and initialise package repositories
  (require 'package)
  (add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
  (package-initialize)

  ;; use-package to simplify the config file
  (unless (package-installed-p 'use-package)
    (package-refresh-contents)
    (package-install 'use-package))
  (require 'use-package)
  (setq use-package-always-ensure 't)

;; Keyboard-centric user interface
  (setq inhibit-startup-message t)
  (tool-bar-mode -1)
  (menu-bar-mode -1)
  (scroll-bar-mode -1)
  (defalias 'yes-or-no-p 'y-or-n-p)

;;practic

(show-paren-mode 1)

(global-display-line-numbers-mode 1)
;; Preset `nlinum-format' for minimum width.
(defun my-nlinum-mode-hook ()
  (when nlinum-mode
    (setq-local nlinum-format
                (concat "%" (number-to-string
                             ;; Guesstimate number of buffer lines.
                             (ceiling (log (max 1 (/ (buffer-size) 80)) 10)))
                        "d"))))
(add-hook 'nlinum-mode-hook #'my-nlinum-mode-hook)

;; auto-completion suggestions in the mini-buffer key-chords -- see if it's preferred over vim-mode
(use-package which-key
    :config
    (which-key-mode)
    (setq which-key-idle-delay 0.5
          which-key-idle-secondary-delay 0.5)
    (which-key-setup-side-window-bottom))

;; Auto completion
  (use-package company
    :config
    (setq company-idle-delay 0
          company-minimum-prefix-length 4
          company-selection-wrap-around t))
  (global-company-mode)

;; 
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes '(xresources))
 '(package-selected-packages
   '(lua-mode evil-matchit powerline-evil evil-org evil-indent-textobject evil-surround evil-leader evil helm which-key use-package dashboard all-the-icons)))

;;fonts
(set-face-attribute 'default nil
  :font "Luxi Mono"
  :height 110
  :weight 'medium)

;; icons and dashboard
(use-package all-the-icons)

(use-package dashboard
  :init      ;; tweak dashboard config before loading it
  (setq dashboard-set-heading-icons t)
  (setq dashboard-set-file-icons t)
  (setq dashboard-banner-logo-title "Emacs Is More Than A Text Editor!")
  ;;(setq dashboard-startup-banner 'logo) ;; use standard emacs logo as banner
  (setq dashboard-startup-banner "~/.emacs.d/emacs-dash5.png")  ;; use custom image as banner
  (setq dashboard-center-content t) ;; set to 't' for centered content
  (setq dashboard-items '((recents . 10)
                          (agenda . 1 )
                          (bookmarks . 1)
                          (projects . 0)
                          (registers . 0)))
  :config
  (dashboard-setup-startup-hook)
  (dashboard-modify-heading-icons '((recents . "file-text")
			      (bookmarks . "book"))))

(delete-selection-mode t)

;; Helm configuration for easyer search
  (use-package helm
    :config
    (require 'helm-config)
    :init
    (helm-mode 1)
    :bind
    (("M-x"     . helm-M-x) ;; Evaluate functions
     ("C-x C-f" . helm-find-files) ;; Open or create files
     ("C-x b"   . helm-mini) ;; Select buffers
     ("C-x C-r" . helm-recentf) ;; Select recently saved files
     ("C-c i"   . helm-imenu) ;; Select document heading
     ("M-y"     . helm-show-kill-ring) ;; Show the kill ring
     :map helm-map
     ("C-z" . helm-select-action)
     ("<tab>" . helm-execute-persistent-action)))

;; evil mode

;; Evil Mode
(use-package evil
  :ensure t
  :config

  (evil-mode 1)
  (use-package evil-leader
    :ensure t
    :config
    (global-evil-leader-mode t)
    (evil-leader/set-leader "<SPC>")
    (evil-leader/set-key
      "s s" 'swiper
      "d x w" 'delete-trailing-whitespace))

  (use-package evil-surround
    :ensure t
    :config (global-evil-surround-mode))

  (use-package evil-indent-textobject
    :ensure t)

  (use-package evil-org
    :ensure t
    :config
    (evil-org-set-key-theme
	  '(textobjects insert navigation additional shift todo heading))
    (add-hook 'org-mode-hook (lambda () (evil-org-mode))))

  (use-package powerline-evil
    :ensure t
    :config
    (powerline-evil-vim-color-theme)))

;;lua-mode

;;(use-package haskell-mode)
(use-package lua-mode)
;;(use-package markdown-mode)
;; (use-package lua-block
;;    :lua-block-mode t)
;;
;; In addition, you can also add one of these too:



(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
