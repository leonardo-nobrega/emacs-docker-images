
;; package repositories
(require 'package)
(add-to-list 'package-archives
             '("melpa" . "https://melpa.org/packages/"))
(package-initialize)

;; do not show menu bar
(tool-bar-mode -1)
(menu-bar-mode -1)

;; magit-status keystroke
(global-set-key (kbd "C-x g") 'magit-status)

;; theme
(modus-themes-select 'modus-vivendi)

;; two lanes on the window
(split-window-horizontally)

;; turn on line wrapping in org
(setq org-startup-truncated nil)

;; org mode code block expansion with "<s TAB"
;; https://emacs.stackexchange.com/a/82500
(require 'org-tempo)

;; this lets me open emacs clients in two or more terminals
(server-start)
