import math
import time
import rospy
import datos
from std_srvs.srv import Empty
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from pynput.keyboard import Key, Listener, KeyCode  # keyboard input


def callback(data):
    print (f"Joint1: {round(math.degrees(data.position[0]),2)} Joint2: {round(math.degrees(data.position[1]),2)} Joint3: {round(math.degrees(data.position[2]),2)} Joint4: {round(math.degrees(data.position[3]),2)} Joint5: {round(math.degrees(data.position[4]),2)}")
    rospy.sleep(3)
            

def listener():
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    #rospy.spin()

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    # Print de comandos
    welcome = """\n 
     ~~~~~~~ Lab. 5 - Cinematica Inversa - Phantom X - ROS ~~~~~~~

Desarrollado por Daniel Cruz y Cristhian Pulido

Para ejecutar la rutina deseada presione la tecla indicada seguida por Enter

            1:  Posición Home   (0, 0, 0, 0, 0.)
            2:  Recoger herramienta
            3:  Delimitar Espacio de trabajo 
            4:  Dibujar Iniciales (D y C)
            5:  Dibujar figuras geométricas:
            6:  Dibujar 5 Puntos 
            7:  Figura Libre (Reliquias de la muerte)
            8:  Descarga Herramienta
                  """
    rospy.loginfo(welcome)
    while not rospy.is_shutdown():
       
        
        key= input()
        i=0
        
        if key == '1':  ##HOME 0 0 0 0 0 
            
            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]
            point = JointTrajectoryPoint()
            point.positions = [math.radians(0), math.radians(0), math.radians(0), math.radians(0), 1]  # 1
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)            
            print('Posición 1: HOME')
            rospy.sleep(1)
            
        if key == '2': ##CARGA HERRAMIENTA 
            inicio2 = time.time()
            for i in range(0,5,1):
                    
                    state = JointTrajectory()
                    state.header.stamp = rospy.Time.now()
                    state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]
                    point = JointTrajectoryPoint()
                    point.positions = datos.F_carga(i) 
                    point.time_from_start = rospy.Duration(0.4)
                    state.points.append(point)
                    pub.publish(state)
                    print(f"Pose: {round(math.degrees(point.positions[0]),2)}, {round(math.degrees(point.positions[1]),2)}, {round(math.degrees(point.positions[2]),2)}, {round(math.degrees(point.positions[3]),2)}, {round(math.degrees(point.positions[4]),2)}  Rutina: Carga de herramienta " )
                    if point.positions[4] > 0.9:
                        print("Herramienta cargada")
                    else:
                        print("Herramienta descargada")
                    rospy.sleep(3)
            print("Rutina < Carga de herramienta > Finalizada")
            fin2 = time.time()
            print(f"Tiempo de ejecución de rutina {fin2-inicio2} s")            

        if key == '3': ##Workspace 
             inicio3 = time.time()
             for i in range(0,12,1):
                    state = JointTrajectory()
                    state.header.stamp = rospy.Time.now()
                    state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]
                    point = JointTrajectoryPoint()
                    point.positions = datos.F_workspace(i)
                    point.time_from_start = rospy.Duration(0.5)
                    state.points.append(point)
                    pub.publish(state)
                    print(f"Pose: {round(math.degrees(point.positions[0]),2)}, {round(math.degrees(point.positions[1]),2)}, {round(math.degrees(point.positions[2]),2)}, {round(math.degrees(point.positions[3]),2)}, {round(math.degrees(point.positions[4]),2)}  Rutina: Delimitación Workspace " )
                    if point.positions[4] > 0.9:
                        print("Herramienta cargada")
                    else:
                        print("Herramienta descargada")
                    rospy.sleep(3)
             print("Rutina < Delimitación Workspace > Finalizada")
             fin3 = time.time()
             print(f"Tiempo de ejecución de rutina {fin3-inicio3} s")            

        if key == '4': ## INICIALES
             inicio4 = time.time()
             for i in range(0,38,1):
                    state = JointTrajectory()
                    state.header.stamp = rospy.Time.now()
                    state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]
                    point = JointTrajectoryPoint()
                    point.positions = datos.F_iniciales(i)
                    point.time_from_start = rospy.Duration(0.5)
                    state.points.append(point)
                    pub.publish(state)
                    print(f"Pose: {round(math.degrees(point.positions[0]),2)}, {round(math.degrees(point.positions[1]),2)}, {round(math.degrees(point.positions[2]),2)}, {round(math.degrees(point.positions[3]),2)}, {round(math.degrees(point.positions[4]),2)}  Rutina: Iniciales " )
                    if point.positions[4] > 0.9:
                        print("Herramienta cargada")
                    else:
                        print("Herramienta descargada")
                    rospy.sleep(3)
             print("Rutina < Iniciales > Finalizada")
             fin4 = time.time()
             print(f"Tiempo de ejecución de rutina {fin4-inicio4} s")            


        if key == '5': ##Figuras
            inicio5 = time.time()
            for i in range(0,108,1):
                    state = JointTrajectory()
                    state.header.stamp = rospy.Time.now()
                    state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]
                    point = JointTrajectoryPoint()
                    point.positions = datos.F_figuras(i) 
                    point.time_from_start = rospy.Duration(0.5)
                    state.points.append(point)
                    pub.publish(state)
                    print(f"Pose: {round(math.degrees(point.positions[0]),2)}, {round(math.degrees(point.positions[1]),2)}, {round(math.degrees(point.positions[2]),2)}, {round(math.degrees(point.positions[3]),2)}, {round(math.degrees(point.positions[4]),2)}  Rutina: Figuras geometricas " )
                    if point.positions[4] > 0.9:
                        print("Herramienta cargada")
                    else:
                        print("Herramienta descargada")
                    rospy.sleep(3)
            print("Rutina < Figuras geometricas > Finalizada")
            fin5 = time.time()
            print(f"Tiempo de ejecución de rutina {fin5-inicio5} s")            

                        
        if key == '6': ##Puntos
            inicio6 = time.time()
            for i in range(0,32,1):
                    state = JointTrajectory()
                    state.header.stamp = rospy.Time.now()
                    state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]
                    point = JointTrajectoryPoint()
                    point.positions = datos.F_puntos(i)
                    point.time_from_start = rospy.Duration(0.5)
                    state.points.append(point)
                    pub.publish(state)
                    print(f"Pose: {round(math.degrees(point.positions[0]),2)}, {round(math.degrees(point.positions[1]),2)}, {round(math.degrees(point.positions[2]),2)}, {round(math.degrees(point.positions[3]),2)}, {round(math.degrees(point.positions[4]),2)}  Rutina: Puntos equidistantes " )
                    if point.positions[4] > 0.9:
                        print("Herramienta cargada")
                    else:
                        print("Herramienta descargada")
                    rospy.sleep(3)
            print("Rutina < Puntos equidistantes > Finalizada")
            fin6 = time.time()
            print(f"Tiempo de ejecución de rutina {fin6-inicio6} s")            


        if key == '7': ##Libre 
            inicio7 = time.time()
            for i in range(0,104,1):
                    state = JointTrajectory()
                    state.header.stamp = rospy.Time.now()
                    state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]
                    point = JointTrajectoryPoint()
                    point.positions = datos.F_libre(i)
                    point.time_from_start = rospy.Duration(0.5)
                    state.points.append(point)
                    pub.publish(state)
                    print(f"Pose: {round(math.degrees(point.positions[0]),2)}, {round(math.degrees(point.positions[1]),2)}, {round(math.degrees(point.positions[2]),2)}, {round(math.degrees(point.positions[3]),2)}, {round(math.degrees(point.positions[4]),2)}  Rutina: Figura libre " )
                    if point.positions[4] > 0.9:
                        print("Herramienta cargada")
                    else:
                        print("Herramienta descargada")
                    rospy.sleep(3)
            print("Rutina < Figura libre (Reliquias de la muerte) >  Finalizada")
            fin7 = time.time()
            print(f"Tiempo de ejecución de rutina {fin7-inicio7} s")            


        if key == '8': ##CARGA HERRAMIENTA 
            inicio8 = time.time()
            for i in range(0,5,1):
                    
                    state = JointTrajectory()
                    state.header.stamp = rospy.Time.now()
                    state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]
                    point = JointTrajectoryPoint()
                    point.positions = datos.F_descargar(i)
                    point.time_from_start = rospy.Duration(0.4)
                    state.points.append(point)
                    pub.publish(state)
                    print(f"Pose: {round(math.degrees(point.positions[0]),2)}, {round(math.degrees(point.positions[1]),2)}, {round(math.degrees(point.positions[2]),2)}, {round(math.degrees(point.positions[3]),2)}, {round(math.degrees(point.positions[4]),2)}  Rutina: Descarga de herramienta " )
                    if point.positions[4] > 0.9:
                        print("Herramienta cargada")
                    else:
                        print("Herramienta descargada")
                    rospy.sleep(3)
            print("Rutina < Descarga de herramienta > Finalizada")
            fin8 = time.time()
            print(f"Tiempo de ejecución de rutina {fin8-inicio8} s")            


        if key == '0':
                listener()

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass
