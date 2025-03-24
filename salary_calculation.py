import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('calcul_salaire.db')
cursor = conn.cursor()

# Mode Debug
DEBUG = True

def debug_print(message):
    if DEBUG:
        print(message)

def calculate_salary(employee_id):
    try:
        cursor.execute('SELECT base_salary FROM employees WHERE id = ?', (employee_id,))
        result = cursor.fetchone()
        
        if result is None:
            print(f"Aucun employé trouvé avec l'ID {employee_id}.")
            return 0
        
        salary = result[0] if result[0] is not None else 0
        
        print(f"\n--- Calcul du salaire pour l'employé ID {employee_id} ---")
        print(f"Salaire de base : {salary}")
        
        # Charger les tâches et actions associées à cet employé
        cursor.execute('''
        SELECT t.id, t.name, a.operation, a.factor, c.condition_type, c.condition_value
        FROM tasks t
        LEFT JOIN actions a ON t.id = a.task_id
        LEFT JOIN conditions c ON t.id = c.task_id
        WHERE t.order_num IS NOT NULL
        ORDER BY t.order_num
        ''')
        tasks = cursor.fetchall()
        
        # Appliquer les actions en fonction des conditions et des opérations
        for task in tasks:
            task_id, task_name, operation, factor, condition_type, condition_value = task
            
            # Remplacer les valeurs None par des valeurs par défaut
            factor = factor if factor is not None else 1.0
            condition_type = condition_type if condition_type is not None else "none"
            condition_value = condition_value if condition_value is not None else 0
            
            debug_print(f"\nTâche : {task_name} (ID : {task_id})")
            debug_print(f"  Action : {operation} (Facteur : {factor})")
            debug_print(f"  Condition : {condition_type} (Valeur : {condition_value})")
            
            # Appliquer l'action
            if operation == 'multiply':
                salary *= factor
            elif operation == 'add':
                salary += factor
            elif operation == 'subtract':
                salary -= factor
            elif operation == 'divide' and factor != 0:
                salary /= factor
            elif operation == 'floor_divide' and factor != 0:
                salary //= factor
            elif operation == 'modulo' and factor != 0:
                salary %= factor
            elif operation == 'exponentiate':
                salary **= factor
            else:
                debug_print("  => Aucune action appliquée.")
            
            debug_print(f"  => Salaire après {operation} : {salary}")
            
            # Vérifier et appliquer les conditions
            if condition_type == 'for' and salary < condition_value:
                debug_print(f"  => Condition remplie : salaire ({salary}) < {condition_value}. Salaire annulé.")
                salary = 0
            else:
                debug_print(f"  => Condition non remplie.")
        
        print(f"\n--- Salaire final pour l'employé ID {employee_id} : {salary} ---")
        return salary
    except sqlite3.Error as e:
        print(f"Erreur SQLite : {e}")
        return 0

# Demander à l'utilisateur de saisir l'ID de l'employé
employee_id = input("Entrez l'ID de l'employé: ")

# Calculer le salaire pour l'ID de l'employé saisi
calculate_salary(employee_id)

# Fermer la connexion à la base de données
conn.close()