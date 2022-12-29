import os as bash

print('El Script de Nopal-vi 🌵')
print('--test: <<el primer paso>> verificar si puede ejecutar correctamente el script')
print('--start: ejecutar el script')
print('--version')
print('--exit: salir')

__version__ = 1.0
__author__ = 'Francisco Griman CEO of Nopal-vi'

def main(command):
    cmd = command

    if cmd != '--test' and cmd != '--start' and cmd != '--version' and cmd != '--exit':
        print('Error de Sintaxis: {}, no existe!'.format(command))
        return main(str(input('>>')))
    
    elif cmd == '--test':
        bash.system('ffmpeg')
    
        try:
            bash.system('clear')
            print('Tienes ffmpeg instalado en tu ordenador!')
    
        except:
            print('Hemos verificado que no tienes ffmpeg en tu ordenador!')
            download = str(input('Deseas instalarlo en el ordenador? [S,s|N,n]: '))
                
            download.upper()
            if download != 'S' and download != 'N':
                bash.system('exit')
    
            elif download == 'S':
                bash.system('sudo snap install ffmpeg')
    
            elif download == 'N':
                print('Es obligatorio para poder ejecutar Nopal-viTools, esperemos ha que vuelvas!')
    
    elif cmd == '--start':
        print('\n --xvids: 256x192 resolución conpleta!')
        print('--xvidsi: 256x144: recomendado por usuarios de Nopal-viTools')
        print('ANTES DE COLOCAR EL COMANDO, EL NOMBRE DEL ARCHIVO DEBE ESTAR COMO nopal-vi.mp4')
        resolution(str(input('\n>>')))
    
    elif cmd == '--version':
        print('\n {} Nopal-viTools [version -sh{}]'.format(colorama.Fore.GREEN, __version__))
        print('{} Creador: {}'.format(colorama.Fore.WHITE, __author__))
    
    elif cmd == '--exit':
        bash.system('exit')

def resolution(format):
    r = format

    if r != '--xvids' and r != '--xvidsi' and r != '--exit':
        print('Error de Sintaxis: {}, no existe!'.format(format))
        return resolution(str(input('>>')))

    elif r == '--xvids':
        bash.system('ffmpeg -i nopal-vi.mp4 -f avi -r 10 -s 256x192 -b 192k -bt 64k -vcodec libxvid -deinterlace -acodec libmp3lame -ar 32000 -ab 96k -ac 2 nopal-vi.avi')
        print('\n\n Listo! Gracias por usar Nopal-viTools^^')
    
    elif r == '--xvidsi':
        bash.system('ffmpeg -i nopal-vi.mp4 -f avi -r 10 -s 256x144 -b 192k -bt 64k -vcodec libxvid -deinterlace -acodec libmp3lame -ar 32000 -ab 96k -ac 2 nopal-vi.avi')
        print('\n\n Listo! Gracias por usar Nopal-viTools^^')
    
    elif r == '--exit':
        bash.system('exit')

if __name__ == '__main__':
    main(str(input('\n>>')))
