import matplotlib.pyplot as plt
import numpy as np

def rotX(point,theta):
    ct=np.cos(theta)
    st=np.sin(theta)
    mat=np.array([[1, 0,  0,   0],
                  [0, ct, -st, 0],
                  [0, st, ct,  0],
                  [0, 0,  0,   1]])
    return np.matmul(mat,point)


def rotY(point,theta):
    ct=np.cos(theta)
    st=np.sin(theta)
    mat=np.array([[ct,  0, st, 0],
                  [0,   1, 0,  0],
                  [-st, 0, ct, 0],
                  [0,   0, 0,  1]])
    return np.matmul(mat,point)


def rotZ(point,theta):
    ct=np.cos(theta)
    st=np.sin(theta)
    mat=np.array([[ct, -st, 0, 0],
                  [st, ct,  0, 0],
                  [0,  0,   1, 0],
                  [0,  0,   0, 1]])
    return np.matmul(mat,point)


def rotAxis(point,point_ref,vec_ref,theta):
    a,b,c=point_ref
    u,v,w=vec_ref/(np.linalg.norm(vec_ref) + 1e-16)
    ct=np.cos(theta)
    st=np.sin(theta)
    R=np.array([[u**2+(v**2+w**2)*ct, u*v*(1-ct)-w*st, u*w*(1-ct)+v*st, (a*(v**2+w**2)-u*(b*v+c*w))*(1-ct)+(b*w-c*v)*st],
               [u*v*(1-ct)+w*st, v**2+(u**2+w**2)*ct, v*w*(1-ct)-u*st, (b*(u**2+w**2)-v*(a*u+c*w))*(1-ct)+(c*u-a*w)*st],
               [u*w*(1-ct)-v*st, v*w*(1-ct)+u*st, w**2+(u**2+v**2)*ct, (c*(u**2+v**2)-w*(a*u+b*v))*(1-ct)+(a*v-b*u)*st],
               [0,0,0,1]])
    return np.matmul(R,point)


def rotation_calculator(point_initial,theta_end,point_ref,vector_ref,k_points,rotation_type):
    dtheta=theta_end/(k_points-1)
    set_points=np.empty([4,0])
    set_points=np.append(set_points,point_initial,axis=1)
    point_current=point_initial

    for i in range(k_points-1):
        if rotation_type=='x':
            point_current=rotX(point_current,dtheta)
        elif rotation_type=='y':
            point_current=rotY(point_current,dtheta)
        elif rotation_type=='z':
            point_current=rotZ(point_current,dtheta)
        elif rotation_type=='custom':
            point_current=rotAxis(point_current,point_ref,vector_ref,dtheta)
        set_points=np.append(set_points,point_current,axis=1)
    return set_points


if __name__ == '__main__':
    #Inputs data
    point_initial=np.array([[2],[2],[2],[1]])
    point_ref=np.array([0.5,1,0]) #only when rotation_type is 'custom'
    vector_ref=np.array([1,0,1])  #only when rotation_type is 'custom'
    k_points=15
    theta_end=3*np.pi/2
    rotation_type='custom' #option: 'x', 'y', 'z' and 'custom'

    #Solving
    set_points=rotation_calculator(point_initial=point_initial,
                                   theta_end=theta_end,
                                   point_ref=point_ref,   #only when rotation_type is 'custom'
                                   vector_ref=vector_ref, #only when rotation_type is 'custom'
                                   k_points=k_points,
                                   rotation_type=rotation_type)
    
    #Plotting
    csfont = {'fontname':'Courier New'}
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection='3d')
    fig.set_facecolor('#c8e1f5ff')
    ax.set_facecolor('#c8e1f5ff')
    plt.title(f'Rotation using the {rotation_type}-axis',fontdict=csfont,fontsize=36)
    ax.quiver(0, 0, 0, 1, 0, 0, length=1, normalize=True,color='red')
    ax.quiver(0, 0, 0, 0, 1, 0, length=1, normalize=True,color='green')
    ax.quiver(0, 0, 0, 0, 0, 1, length=1, normalize=True,color='blue')
    if rotation_type=='custom':
        ax.quiver(*point_ref, *vector_ref, length=1, normalize=True, color='orange')
    ax.set_xlabel('X-axis',fontdict=csfont,fontsize=30)
    ax.set_ylabel('Y-axis',fontdict=csfont,fontsize=30)
    ax.set_zlabel('Z-axis',fontdict=csfont,fontsize=30)
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.set_zlim(-5,5)
    color_pallete=np.linspace(127,0,k_points,True)/255
    size_points=np.linspace(8,14,k_points,True)**2
    ax.scatter(set_points[0,:],set_points[1,:],set_points[2,:],c=[(j,j,j) for j in color_pallete],s=size_points)
    plt.show()