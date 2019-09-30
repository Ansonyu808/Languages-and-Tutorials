# PHP

### Credit to W3 Schools


### Vim Config: 
I Used these settings to run my php commands better.
* In the terminal install the php cli
	* For Debian and Ubuntu users: something like ```sudo apt install php7.2-cli``` and the corresponding MySQLi client ```sudo apt install php7.2-mysqli```
* Plugins: StanAngeloff/php.vim
* Remaps: allows you to run code in vim (in the vimrc)
	*  ```autocmd FileType php nmap <leader>lr :!php %<CR>```
