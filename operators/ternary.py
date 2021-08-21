# Não segue a estrutura <condicional> ? <true> : <false>
lockdown = True
status = 'Em casa' if lockdown else 'Pode sair'
print(status)

lockdown = False
status = 'Em casa' if lockdown else 'Pode sair'
print(status)