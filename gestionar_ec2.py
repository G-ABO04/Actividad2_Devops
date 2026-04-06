import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

def listar_instancias():
    try:
        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"ID: {instance['InstanceId']} - Estado: {instance['State']['Name']}")
    except Exception as e:
        print(f"Error: {e}")

def gestionar_instancia(instance_id, accion):
    try:
        if accion == "iniciar":
            ec2.start_instances(InstanceIds=[instance_id])
            print(f"Instancia {instance_id} iniciada")
        elif accion == "detener":
            ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Instancia {instance_id} detenida")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    listar_instancias()

    gestionar_instancia("i-047e10030ea1b634c", "detener")
