CREATE TABLE liske (
    id_liske INT AUTOINCREMENT PRIMARY KEY,
    liske_name TEXT
);

CREATE TABLE task (
    id_task INT AUTOINCREMENT PRIMARY KEY,
    task_name TEXT,
    task_priority INT,
    task_liske INT,

    FOREIGN KEY (task_liske) REFERENCES liske (id_liske)
);