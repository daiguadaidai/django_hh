CREATE DATABASE blog;

CREATE TABLE employee(
    employee_id BIGINT unsigned NOT NULL AUTO_INCREMENT COMMENT '员工ID',
    name VARCHAR(10) NOT NULL DEFAULT '' COMMENT '员工姓名',
    age TINYINT unsigned NOT NULL DEFAULT 0 COMMENT '员工年龄',
    gender TINYINT unsigned NOT NULL DEFAULT 1 COMMENT '性别: 1、男，2、女、3、其他',
    dept_id BIGINT NOT unsigned NOT NULL COMMENT '部门ID',
    create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY(employee_id),
    UNIQUE INDEX udx$name(name),
    INDEX idx$dept_id(dept_id)
)COMMENT = '员工表';

ALTER TABLE employee
    ADD dept_id BIGINT unsigned NOT NULL COMMENT '部门ID' AFTER gender,
    ADD INDEX idx$dept_id(dept_id);

CREATE TABLE dept(
    dept_id BIGINT unsigned NOT NULL AUTO_INCREMENT COMMENT '部门ID',
    name VARCHAR(10) NOT NULL DEFAULT '' COMMENT '部门名称',
    dept_code VARCHAR(5) NOT NULL DEFAULT '' COMMENT '部门编码',
    create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY(dept_id),
    UNIQUE INDEX udx$name(name),
    UNIQUE INDEX udx$dept_code(dept_code)
) COMMENT = '部门表';

CREATE TABLE engine(
    engine_id INT unsigned NOT NULL AUTO_INCREMENT COMMENT '引擎ID',
    code VARCHAR(5) NOT NULL DEFAULT '' COMMENT '引擎编码',
    create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY(engine_id),
    UNIQUE INDEX udx$code(code)
) COMMENT = '引擎表';

CREATE TABLE car(
    car_id INT unsigned NOT NULL AUTO_INCREMENT COMMENT '车ID',
    engine_id INT unsigned NOT NULL COMMENT '引擎ID',
    name VARCHAR(5) NOT NULL DEFAULT '' COMMENT '车名字',
    create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY(car_id),
    INDEX idx$engine_id(engine_id),
    UNIQUE INDEX udx$name(name)
) COMMENT = '车表';
