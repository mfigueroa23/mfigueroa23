Create database cinestudio;
use cinestudio;
create table Peliculas (
    id serial, 
    Nombre varchar(100),
    Descripcion varchar(255),
    Fecha date,
    Categoria varchar (100),
    Precio int,
    primary key (id)
);