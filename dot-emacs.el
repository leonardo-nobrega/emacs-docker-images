
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

;; this lets me open emacs clients in two or more terminals
(server-start)
