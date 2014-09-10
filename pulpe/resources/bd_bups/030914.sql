--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.5
-- Dumped by pg_dump version 9.3.5
-- Started on 2014-09-10 16:50:13

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 205 (class 3079 OID 11750)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2186 (class 0 OID 0)
-- Dependencies: 205
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 177 (class 1259 OID 16433)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- TOC entry 176 (class 1259 OID 16431)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- TOC entry 2187 (class 0 OID 0)
-- Dependencies: 176
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- TOC entry 175 (class 1259 OID 16418)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- TOC entry 174 (class 1259 OID 16416)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 2188 (class 0 OID 0)
-- Dependencies: 174
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- TOC entry 173 (class 1259 OID 16408)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- TOC entry 172 (class 1259 OID 16406)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- TOC entry 2189 (class 0 OID 0)
-- Dependencies: 172
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- TOC entry 183 (class 1259 OID 16478)
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- TOC entry 179 (class 1259 OID 16448)
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- TOC entry 178 (class 1259 OID 16446)
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- TOC entry 2190 (class 0 OID 0)
-- Dependencies: 178
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- TOC entry 182 (class 1259 OID 16476)
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- TOC entry 2191 (class 0 OID 0)
-- Dependencies: 182
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- TOC entry 181 (class 1259 OID 16463)
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- TOC entry 180 (class 1259 OID 16461)
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 2192 (class 0 OID 0)
-- Dependencies: 180
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- TOC entry 188 (class 1259 OID 16545)
-- Name: clientes_cliente; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE clientes_cliente (
    id integer NOT NULL,
    nombre character varying(250) NOT NULL,
    apellido character varying(250) NOT NULL,
    cargo character varying(150) NOT NULL,
    celular character varying(8) NOT NULL,
    correo character varying(70) NOT NULL
);


ALTER TABLE public.clientes_cliente OWNER TO postgres;

--
-- TOC entry 187 (class 1259 OID 16543)
-- Name: clientes_cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE clientes_cliente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clientes_cliente_id_seq OWNER TO postgres;

--
-- TOC entry 2193 (class 0 OID 0)
-- Dependencies: 187
-- Name: clientes_cliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE clientes_cliente_id_seq OWNED BY clientes_cliente.id;


--
-- TOC entry 171 (class 1259 OID 16396)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- TOC entry 170 (class 1259 OID 16394)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- TOC entry 2194 (class 0 OID 0)
-- Dependencies: 170
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- TOC entry 185 (class 1259 OID 16503)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- TOC entry 184 (class 1259 OID 16501)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- TOC entry 2195 (class 0 OID 0)
-- Dependencies: 184
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- TOC entry 186 (class 1259 OID 16521)
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- TOC entry 192 (class 1259 OID 16569)
-- Name: facturas_factura; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE facturas_factura (
    id integer NOT NULL,
    cliente_id integer NOT NULL,
    estado integer NOT NULL,
    fecha_apertura date NOT NULL,
    fecha_cierra date
);


ALTER TABLE public.facturas_factura OWNER TO postgres;

--
-- TOC entry 191 (class 1259 OID 16567)
-- Name: facturas_factura_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE facturas_factura_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.facturas_factura_id_seq OWNER TO postgres;

--
-- TOC entry 2196 (class 0 OID 0)
-- Dependencies: 191
-- Name: facturas_factura_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE facturas_factura_id_seq OWNED BY facturas_factura.id;


--
-- TOC entry 194 (class 1259 OID 16582)
-- Name: facturas_producto_factura; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE facturas_producto_factura (
    id integer NOT NULL,
    factura_id integer NOT NULL,
    producto_id integer NOT NULL,
    precio_actual numeric(6,2) NOT NULL,
    cantidad integer NOT NULL,
    subtotal numeric(6,2) NOT NULL
);


ALTER TABLE public.facturas_producto_factura OWNER TO postgres;

--
-- TOC entry 193 (class 1259 OID 16580)
-- Name: facturas_producto_factura_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE facturas_producto_factura_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.facturas_producto_factura_id_seq OWNER TO postgres;

--
-- TOC entry 2197 (class 0 OID 0)
-- Dependencies: 193
-- Name: facturas_producto_factura_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE facturas_producto_factura_id_seq OWNED BY facturas_producto_factura.id;


--
-- TOC entry 198 (class 1259 OID 16617)
-- Name: inventario_compra; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_compra (
    id integer NOT NULL,
    fecha date NOT NULL,
    total_compra numeric(6,2) NOT NULL
);


ALTER TABLE public.inventario_compra OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 16615)
-- Name: inventario_compra_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_compra_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_compra_id_seq OWNER TO postgres;

--
-- TOC entry 2198 (class 0 OID 0)
-- Dependencies: 197
-- Name: inventario_compra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_compra_id_seq OWNED BY inventario_compra.id;


--
-- TOC entry 196 (class 1259 OID 16604)
-- Name: inventario_disponibilidad; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_disponibilidad (
    id integer NOT NULL,
    producto_id integer NOT NULL,
    cantidad integer NOT NULL
);


ALTER TABLE public.inventario_disponibilidad OWNER TO postgres;

--
-- TOC entry 195 (class 1259 OID 16602)
-- Name: inventario_disponibilidad_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_disponibilidad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_disponibilidad_id_seq OWNER TO postgres;

--
-- TOC entry 2199 (class 0 OID 0)
-- Dependencies: 195
-- Name: inventario_disponibilidad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_disponibilidad_id_seq OWNED BY inventario_disponibilidad.id;


--
-- TOC entry 190 (class 1259 OID 16558)
-- Name: inventario_producto; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_producto (
    id integer NOT NULL,
    nombre character varying(250) NOT NULL,
    marca character varying(150) NOT NULL,
    detalles character varying(500) NOT NULL,
    proveedor character varying(250) NOT NULL,
    costo numeric(6,2) NOT NULL,
    precio numeric(6,2) NOT NULL,
    imagen character varying(100),
    categoria character varying(2) NOT NULL
);


ALTER TABLE public.inventario_producto OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16643)
-- Name: inventario_producto_abastecimiento; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_producto_abastecimiento (
    id integer NOT NULL,
    producto_id integer NOT NULL,
    minimo integer NOT NULL
);


ALTER TABLE public.inventario_producto_abastecimiento OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16641)
-- Name: inventario_producto_abastecimiento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_producto_abastecimiento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_producto_abastecimiento_id_seq OWNER TO postgres;

--
-- TOC entry 2200 (class 0 OID 0)
-- Dependencies: 201
-- Name: inventario_producto_abastecimiento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_producto_abastecimiento_id_seq OWNED BY inventario_producto_abastecimiento.id;


--
-- TOC entry 200 (class 1259 OID 16625)
-- Name: inventario_producto_compra; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_producto_compra (
    id integer NOT NULL,
    compra_id integer NOT NULL,
    producto_id integer NOT NULL,
    cantidad integer NOT NULL,
    costo numeric(6,2) NOT NULL
);


ALTER TABLE public.inventario_producto_compra OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 16623)
-- Name: inventario_producto_compra_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_producto_compra_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_producto_compra_id_seq OWNER TO postgres;

--
-- TOC entry 2201 (class 0 OID 0)
-- Dependencies: 199
-- Name: inventario_producto_compra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_producto_compra_id_seq OWNED BY inventario_producto_compra.id;


--
-- TOC entry 189 (class 1259 OID 16556)
-- Name: inventario_producto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_producto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_producto_id_seq OWNER TO postgres;

--
-- TOC entry 2202 (class 0 OID 0)
-- Dependencies: 189
-- Name: inventario_producto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_producto_id_seq OWNED BY inventario_producto.id;


--
-- TOC entry 204 (class 1259 OID 16660)
-- Name: south_migrationhistory; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE south_migrationhistory (
    id integer NOT NULL,
    app_name character varying(255) NOT NULL,
    migration character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.south_migrationhistory OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16658)
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE south_migrationhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.south_migrationhistory_id_seq OWNER TO postgres;

--
-- TOC entry 2203 (class 0 OID 0)
-- Dependencies: 203
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE south_migrationhistory_id_seq OWNED BY south_migrationhistory.id;


--
-- TOC entry 1932 (class 2604 OID 16436)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- TOC entry 1931 (class 2604 OID 16421)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 1930 (class 2604 OID 16411)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- TOC entry 1935 (class 2604 OID 16481)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- TOC entry 1933 (class 2604 OID 16451)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- TOC entry 1934 (class 2604 OID 16466)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- TOC entry 1937 (class 2604 OID 16548)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY clientes_cliente ALTER COLUMN id SET DEFAULT nextval('clientes_cliente_id_seq'::regclass);


--
-- TOC entry 1928 (class 2604 OID 16399)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- TOC entry 1936 (class 2604 OID 16506)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- TOC entry 1939 (class 2604 OID 16572)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY facturas_factura ALTER COLUMN id SET DEFAULT nextval('facturas_factura_id_seq'::regclass);


--
-- TOC entry 1940 (class 2604 OID 16585)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY facturas_producto_factura ALTER COLUMN id SET DEFAULT nextval('facturas_producto_factura_id_seq'::regclass);


--
-- TOC entry 1942 (class 2604 OID 16620)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_compra ALTER COLUMN id SET DEFAULT nextval('inventario_compra_id_seq'::regclass);


--
-- TOC entry 1941 (class 2604 OID 16607)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_disponibilidad ALTER COLUMN id SET DEFAULT nextval('inventario_disponibilidad_id_seq'::regclass);


--
-- TOC entry 1938 (class 2604 OID 16561)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_producto ALTER COLUMN id SET DEFAULT nextval('inventario_producto_id_seq'::regclass);


--
-- TOC entry 1944 (class 2604 OID 16646)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_producto_abastecimiento ALTER COLUMN id SET DEFAULT nextval('inventario_producto_abastecimiento_id_seq'::regclass);


--
-- TOC entry 1943 (class 2604 OID 16628)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_producto_compra ALTER COLUMN id SET DEFAULT nextval('inventario_producto_compra_id_seq'::regclass);


--
-- TOC entry 1945 (class 2604 OID 16663)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY south_migrationhistory ALTER COLUMN id SET DEFAULT nextval('south_migrationhistory_id_seq'::regclass);


--
-- TOC entry 2151 (class 0 OID 16433)
-- Dependencies: 177
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- TOC entry 2204 (class 0 OID 0)
-- Dependencies: 176
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- TOC entry 2149 (class 0 OID 16418)
-- Dependencies: 175
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- TOC entry 2205 (class 0 OID 0)
-- Dependencies: 174
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 2147 (class 0 OID 16408)
-- Dependencies: 173
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add cliente	7	add_cliente
20	Can change cliente	7	change_cliente
21	Can delete cliente	7	delete_cliente
22	Can add producto	8	add_producto
23	Can change producto	8	change_producto
24	Can delete producto	8	delete_producto
25	Can add factura	9	add_factura
26	Can change factura	9	change_factura
27	Can delete factura	9	delete_factura
28	Can add producto_factura	10	add_producto_factura
29	Can change producto_factura	10	change_producto_factura
30	Can delete producto_factura	10	delete_producto_factura
31	Can add disponibilidad	11	add_disponibilidad
32	Can change disponibilidad	11	change_disponibilidad
33	Can delete disponibilidad	11	delete_disponibilidad
34	Can add compra	12	add_compra
35	Can change compra	12	change_compra
36	Can delete compra	12	delete_compra
37	Can add producto_compra	13	add_producto_compra
38	Can change producto_compra	13	change_producto_compra
39	Can delete producto_compra	13	delete_producto_compra
40	Can add producto_abastecimiento	14	add_producto_abastecimiento
41	Can change producto_abastecimiento	14	change_producto_abastecimiento
42	Can delete producto_abastecimiento	14	delete_producto_abastecimiento
43	Can add migration history	15	add_migrationhistory
44	Can change migration history	15	change_migrationhistory
45	Can delete migration history	15	delete_migrationhistory
\.


--
-- TOC entry 2206 (class 0 OID 0)
-- Dependencies: 172
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 45, true);


--
-- TOC entry 2157 (class 0 OID 16478)
-- Dependencies: 183
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$12000$uwcYlOJJYqAy$yWU20/79j6hsFLkiqmpA1gqt0YQAkCLpU84ODjzTMQQ=	2014-09-03 16:42:01.715-06	t	rardon			rolando_ardon299@hotmail.com	t	t	2014-09-03 16:41:27.544-06
\.


--
-- TOC entry 2153 (class 0 OID 16448)
-- Dependencies: 179
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 178
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 182
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- TOC entry 2155 (class 0 OID 16463)
-- Dependencies: 181
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 2209 (class 0 OID 0)
-- Dependencies: 180
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 2162 (class 0 OID 16545)
-- Dependencies: 188
-- Data for Name: clientes_cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY clientes_cliente (id, nombre, apellido, cargo, celular, correo) FROM stdin;
\.


--
-- TOC entry 2210 (class 0 OID 0)
-- Dependencies: 187
-- Name: clientes_cliente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('clientes_cliente_id_seq', 1, false);


--
-- TOC entry 2145 (class 0 OID 16396)
-- Dependencies: 171
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2014-09-03 17:33:03.667-06	1	8	1	producto object	1	
2	2014-09-03 17:33:56.279-06	1	8	2	producto object	1	
3	2014-09-03 17:40:38.63-06	1	12	1	2014-09-02	1	
4	2014-09-03 17:41:11.418-06	1	13	1	[2014-09-02] Churro Frito Lay	1	
5	2014-09-03 17:41:36.185-06	1	13	2	[2014-09-02] Churro Sabritas	1	
6	2014-09-03 17:43:13.522-06	1	14	1	Churro Frito Lay	1	
7	2014-09-03 17:43:18.13-06	1	14	2	Churro Sabritas	1	
8	2014-09-03 17:52:47.139-06	1	13	2	[2014-09-02] Churro Sabritas	3	
9	2014-09-03 17:52:47.242-06	1	13	1	[2014-09-02] Churro Frito Lay	3	
10	2014-09-03 17:53:15.482-06	1	13	3	[2014-09-02] Churro Frito Lay	1	
11	2014-09-03 17:53:31.701-06	1	13	4	[2014-09-02] Churro Sabritas	1	
12	2014-09-08 16:14:26.3-06	1	8	2	Churro Sabritas	2	No fields changed.
13	2014-09-08 16:14:56.241-06	1	8	2	Churro Sabritas	2	Changed imagen.
14	2014-09-08 16:15:02.295-06	1	8	1	Churro Frito Lay	2	Changed imagen.
15	2014-09-08 16:15:39.738-06	1	8	1	Churro Frito Lay	2	Changed imagen.
16	2014-09-08 16:37:31.905-06	1	8	1	Churro Frito Lay	2	Changed imagen.
17	2014-09-09 14:23:55.822-06	1	8	3	CocaCola 	1	
18	2014-09-09 14:24:53.485-06	1	8	4	Te Lipton	1	
19	2014-09-09 14:25:48.489-06	1	8	5	Galleta Oreo	1	
20	2014-09-09 14:26:33.521-06	1	8	6	Marshmellow	1	
21	2014-09-10 09:44:15.608-06	1	12	2	2014-09-09	1	
22	2014-09-10 09:45:32.804-06	1	8	7	Air Head Little	1	
23	2014-09-10 09:46:54.216-06	1	8	8	Galleta Bridge	1	
24	2014-09-10 09:48:18.779-06	1	8	9	Paleta Jolly Rancher	1	
25	2014-09-10 11:03:30.951-06	1	12	3	2014-09-10	1	
\.


--
-- TOC entry 2211 (class 0 OID 0)
-- Dependencies: 170
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 25, true);


--
-- TOC entry 2159 (class 0 OID 16503)
-- Dependencies: 185
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	log entry	admin	logentry
2	permission	auth	permission
3	group	auth	group
4	user	auth	user
5	content type	contenttypes	contenttype
6	session	sessions	session
7	cliente	clientes	cliente
8	producto	inventario	producto
9	factura	facturas	factura
10	producto_factura	facturas	producto_factura
11	disponibilidad	inventario	disponibilidad
12	compra	inventario	compra
13	producto_compra	inventario	producto_compra
14	producto_abastecimiento	inventario	producto_abastecimiento
15	migration history	south	migrationhistory
\.


--
-- TOC entry 2212 (class 0 OID 0)
-- Dependencies: 184
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 15, true);


--
-- TOC entry 2160 (class 0 OID 16521)
-- Dependencies: 186
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
upuw6vtmlwltv17jahfk35wiq3mod54d	NjQxZmQwZDY1YjdkOWUxNWVlNTVhOTQ2M2ViYjYyMmY1MzUwMGI0ZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=	2014-09-17 16:42:01.718-06
\.


--
-- TOC entry 2166 (class 0 OID 16569)
-- Dependencies: 192
-- Data for Name: facturas_factura; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY facturas_factura (id, cliente_id, estado, fecha_apertura, fecha_cierra) FROM stdin;
\.


--
-- TOC entry 2213 (class 0 OID 0)
-- Dependencies: 191
-- Name: facturas_factura_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('facturas_factura_id_seq', 1, false);


--
-- TOC entry 2168 (class 0 OID 16582)
-- Dependencies: 194
-- Data for Name: facturas_producto_factura; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY facturas_producto_factura (id, factura_id, producto_id, precio_actual, cantidad, subtotal) FROM stdin;
\.


--
-- TOC entry 2214 (class 0 OID 0)
-- Dependencies: 193
-- Name: facturas_producto_factura_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('facturas_producto_factura_id_seq', 1, false);


--
-- TOC entry 2172 (class 0 OID 16617)
-- Dependencies: 198
-- Data for Name: inventario_compra; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_compra (id, fecha, total_compra) FROM stdin;
1	2014-09-02	542.90
2	2014-09-09	689.80
3	2014-09-10	242.00
\.


--
-- TOC entry 2215 (class 0 OID 0)
-- Dependencies: 197
-- Name: inventario_compra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_compra_id_seq', 3, true);


--
-- TOC entry 2170 (class 0 OID 16604)
-- Dependencies: 196
-- Data for Name: inventario_disponibilidad; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_disponibilidad (id, producto_id, cantidad) FROM stdin;
2	1	50
3	2	35
4	3	12
5	4	24
6	5	36
7	6	50
8	7	28
9	8	20
10	9	28
\.


--
-- TOC entry 2216 (class 0 OID 0)
-- Dependencies: 195
-- Name: inventario_disponibilidad_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_disponibilidad_id_seq', 10, true);


--
-- TOC entry 2164 (class 0 OID 16558)
-- Dependencies: 190
-- Data for Name: inventario_producto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_producto (id, nombre, marca, detalles, proveedor, costo, precio, imagen, categoria) FROM stdin;
2	Churro Sabritas	Sabritas	Churro Variado	PRICESMART	4.90	8.00		O
1	Churro Frito Lay	Frito Lay	Churro de importación	PRICESMART	7.40	10.00	resources/imgs/productos/FritoLays.jpg	O
3	CocaCola 	CocaCola 	600ml	PRICESMART	11.40	15.00		O
4	Te Lipton	Lipton	500ml	PRICESMART	13.00	18.00		O
5	Galleta Oreo	Oreo	Presentación de 4 galletas	PRICESMART	3.70	8.00		O
6	Marshmellow	Angelitos	Bolsita de mini-marshmellows	PRICESMART	2.10	5.00		O
7	Air Head Little	Air Head	Presentación pequeña	ALMACENES XTRA	3.40	5.00		O
8	Galleta Bridge	Bridge	Galletas variadas tipo wafle	ALMACENES XTRA	2.90	6.00		O
9	Paleta Jolly Rancher	Jolly Rancher	Paleta variada en forma de corazón	ALMACENES XTRA	3.20	5.00		O
\.


--
-- TOC entry 2176 (class 0 OID 16643)
-- Dependencies: 202
-- Data for Name: inventario_producto_abastecimiento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_producto_abastecimiento (id, producto_id, minimo) FROM stdin;
1	1	5
2	2	5
\.


--
-- TOC entry 2217 (class 0 OID 0)
-- Dependencies: 201
-- Name: inventario_producto_abastecimiento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_producto_abastecimiento_id_seq', 2, true);


--
-- TOC entry 2174 (class 0 OID 16625)
-- Dependencies: 200
-- Data for Name: inventario_producto_compra; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_producto_compra (id, compra_id, producto_id, cantidad, costo) FROM stdin;
3	1	1	50	7.40
4	1	2	35	4.90
5	2	3	12	136.95
6	2	4	24	314.95
7	2	5	36	132.95
8	2	6	50	104.95
9	3	7	28	3.40
10	3	8	20	2.90
11	3	9	28	3.20
\.


--
-- TOC entry 2218 (class 0 OID 0)
-- Dependencies: 199
-- Name: inventario_producto_compra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_producto_compra_id_seq', 11, true);


--
-- TOC entry 2219 (class 0 OID 0)
-- Dependencies: 189
-- Name: inventario_producto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_producto_id_seq', 9, true);


--
-- TOC entry 2178 (class 0 OID 16660)
-- Dependencies: 204
-- Data for Name: south_migrationhistory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY south_migrationhistory (id, app_name, migration, applied) FROM stdin;
1	inventario	0002_auto__del_field_producto_cantidad	2014-09-03 17:31:28.609-06
2	inventario	0003_auto__add_field_producto_imagen	2014-09-05 15:17:57.107-06
3	inventario	0004_auto__add_unique_disponibilidad_producto	2014-09-09 14:22:10.514-06
4	inventario	0005_auto__chg_field_producto_imagen	2014-09-09 14:23:42.662-06
5	inventario	0006_auto__add_field_producto_categoria	2014-09-10 11:00:04.263-06
\.


--
-- TOC entry 2220 (class 0 OID 0)
-- Dependencies: 203
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('south_migrationhistory_id_seq', 5, true);


--
-- TOC entry 1962 (class 2606 OID 16440)
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 1957 (class 2606 OID 16425)
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- TOC entry 1960 (class 2606 OID 16423)
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 1965 (class 2606 OID 16438)
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 1952 (class 2606 OID 16415)
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- TOC entry 1954 (class 2606 OID 16413)
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 1968 (class 2606 OID 16453)
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 1971 (class 2606 OID 16455)
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- TOC entry 1979 (class 2606 OID 16483)
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 1974 (class 2606 OID 16468)
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 1977 (class 2606 OID 16470)
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- TOC entry 1981 (class 2606 OID 16485)
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 1992 (class 2606 OID 16555)
-- Name: clientes_cliente_correo_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY clientes_cliente
    ADD CONSTRAINT clientes_cliente_correo_key UNIQUE (correo);


--
-- TOC entry 1995 (class 2606 OID 16553)
-- Name: clientes_cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY clientes_cliente
    ADD CONSTRAINT clientes_cliente_pkey PRIMARY KEY (id);


--
-- TOC entry 1948 (class 2606 OID 16405)
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 1984 (class 2606 OID 16510)
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- TOC entry 1986 (class 2606 OID 16508)
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 1989 (class 2606 OID 16528)
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 2000 (class 2606 OID 16574)
-- Name: facturas_factura_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY facturas_factura
    ADD CONSTRAINT facturas_factura_pkey PRIMARY KEY (id);


--
-- TOC entry 2003 (class 2606 OID 16587)
-- Name: facturas_producto_factura_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY facturas_producto_factura
    ADD CONSTRAINT facturas_producto_factura_pkey PRIMARY KEY (id);


--
-- TOC entry 2011 (class 2606 OID 16622)
-- Name: inventario_compra_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_compra
    ADD CONSTRAINT inventario_compra_pkey PRIMARY KEY (id);


--
-- TOC entry 2006 (class 2606 OID 16609)
-- Name: inventario_disponibilidad_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_disponibilidad
    ADD CONSTRAINT inventario_disponibilidad_pkey PRIMARY KEY (id);


--
-- TOC entry 2009 (class 2606 OID 24597)
-- Name: inventario_disponibilidad_producto_id_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_disponibilidad
    ADD CONSTRAINT inventario_disponibilidad_producto_id_uniq UNIQUE (producto_id);


--
-- TOC entry 2017 (class 2606 OID 16648)
-- Name: inventario_producto_abastecimiento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_producto_abastecimiento
    ADD CONSTRAINT inventario_producto_abastecimiento_pkey PRIMARY KEY (id);


--
-- TOC entry 2014 (class 2606 OID 16630)
-- Name: inventario_producto_compra_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_producto_compra
    ADD CONSTRAINT inventario_producto_compra_pkey PRIMARY KEY (id);


--
-- TOC entry 1997 (class 2606 OID 16566)
-- Name: inventario_producto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_producto
    ADD CONSTRAINT inventario_producto_pkey PRIMARY KEY (id);


--
-- TOC entry 2020 (class 2606 OID 16668)
-- Name: south_migrationhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY south_migrationhistory
    ADD CONSTRAINT south_migrationhistory_pkey PRIMARY KEY (id);


--
-- TOC entry 1963 (class 1259 OID 16534)
-- Name: auth_group_name_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_name_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 1955 (class 1259 OID 16532)
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- TOC entry 1958 (class 1259 OID 16533)
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- TOC entry 1950 (class 1259 OID 16531)
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- TOC entry 1966 (class 1259 OID 16536)
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- TOC entry 1969 (class 1259 OID 16535)
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- TOC entry 1972 (class 1259 OID 16538)
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- TOC entry 1975 (class 1259 OID 16537)
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- TOC entry 1982 (class 1259 OID 16539)
-- Name: auth_user_username_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_username_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 1993 (class 1259 OID 16598)
-- Name: clientes_cliente_correo_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX clientes_cliente_correo_like ON clientes_cliente USING btree (correo varchar_pattern_ops);


--
-- TOC entry 1946 (class 1259 OID 16530)
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- TOC entry 1949 (class 1259 OID 16529)
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- TOC entry 1987 (class 1259 OID 16541)
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- TOC entry 1990 (class 1259 OID 16540)
-- Name: django_session_session_key_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 1998 (class 1259 OID 16599)
-- Name: facturas_factura_cliente_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX facturas_factura_cliente_id ON facturas_factura USING btree (cliente_id);


--
-- TOC entry 2001 (class 1259 OID 16600)
-- Name: facturas_producto_factura_factura_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX facturas_producto_factura_factura_id ON facturas_producto_factura USING btree (factura_id);


--
-- TOC entry 2004 (class 1259 OID 16601)
-- Name: facturas_producto_factura_producto_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX facturas_producto_factura_producto_id ON facturas_producto_factura USING btree (producto_id);


--
-- TOC entry 2007 (class 1259 OID 16654)
-- Name: inventario_disponibilidad_producto_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_disponibilidad_producto_id ON inventario_disponibilidad USING btree (producto_id);


--
-- TOC entry 2018 (class 1259 OID 16657)
-- Name: inventario_producto_abastecimiento_producto_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_producto_abastecimiento_producto_id ON inventario_producto_abastecimiento USING btree (producto_id);


--
-- TOC entry 2012 (class 1259 OID 16655)
-- Name: inventario_producto_compra_compra_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_producto_compra_compra_id ON inventario_producto_compra USING btree (compra_id);


--
-- TOC entry 2015 (class 1259 OID 16656)
-- Name: inventario_producto_compra_producto_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_producto_compra_producto_id ON inventario_producto_compra USING btree (producto_id);


--
-- TOC entry 2024 (class 2606 OID 16426)
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2026 (class 2606 OID 16456)
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2028 (class 2606 OID 16471)
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2022 (class 2606 OID 16511)
-- Name: content_type_id_refs_id_93d2d1f8; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT content_type_id_refs_id_93d2d1f8 FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2023 (class 2606 OID 16516)
-- Name: content_type_id_refs_id_d043b34a; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2030 (class 2606 OID 16575)
-- Name: facturas_factura_cliente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY facturas_factura
    ADD CONSTRAINT facturas_factura_cliente_id_fkey FOREIGN KEY (cliente_id) REFERENCES clientes_cliente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2031 (class 2606 OID 16588)
-- Name: facturas_producto_factura_factura_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY facturas_producto_factura
    ADD CONSTRAINT facturas_producto_factura_factura_id_fkey FOREIGN KEY (factura_id) REFERENCES facturas_factura(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2032 (class 2606 OID 16593)
-- Name: facturas_producto_factura_producto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY facturas_producto_factura
    ADD CONSTRAINT facturas_producto_factura_producto_id_fkey FOREIGN KEY (producto_id) REFERENCES inventario_producto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2025 (class 2606 OID 16441)
-- Name: group_id_refs_id_f4b32aac; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2033 (class 2606 OID 16610)
-- Name: inventario_disponibilidad_producto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_disponibilidad
    ADD CONSTRAINT inventario_disponibilidad_producto_id_fkey FOREIGN KEY (producto_id) REFERENCES inventario_producto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2036 (class 2606 OID 16649)
-- Name: inventario_producto_abastecimiento_producto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_producto_abastecimiento
    ADD CONSTRAINT inventario_producto_abastecimiento_producto_id_fkey FOREIGN KEY (producto_id) REFERENCES inventario_producto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2034 (class 2606 OID 16631)
-- Name: inventario_producto_compra_compra_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_producto_compra
    ADD CONSTRAINT inventario_producto_compra_compra_id_fkey FOREIGN KEY (compra_id) REFERENCES inventario_compra(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2035 (class 2606 OID 16636)
-- Name: inventario_producto_compra_producto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_producto_compra
    ADD CONSTRAINT inventario_producto_compra_producto_id_fkey FOREIGN KEY (producto_id) REFERENCES inventario_producto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2027 (class 2606 OID 16491)
-- Name: user_id_refs_id_40c41112; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_40c41112 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2029 (class 2606 OID 16496)
-- Name: user_id_refs_id_4dc23c39; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_4dc23c39 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2021 (class 2606 OID 16486)
-- Name: user_id_refs_id_c0d12874; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT user_id_refs_id_c0d12874 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2185 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2014-09-10 16:50:18

--
-- PostgreSQL database dump complete
--
