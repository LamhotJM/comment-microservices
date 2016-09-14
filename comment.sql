CREATE TABLE comments (
    commentid SERIAL,
    userid character varying(100),
    loanid character varying(100),
    comment  TEXT,
    createdby character varying(60) NOT NULL,
    createddate timestamp without time zone NOT NULL,
    createdfrom character varying(25) NOT NULL,
    modifiedby character varying(60),
    modifieddate timestamp without time zone,
    modifiedfrom character varying(25),
     PRIMARY KEY (commentid )
    )



INSERT INTO public.comments(
            userid, loanid, comment, createdby, createddate,
            createdfrom, modifiedby, modifieddate, modifiedfrom)
    VALUES ( 1, 1, 'lorem ipsum', 'createdby Jhon Doe', '2038-01-19 03:14:07', 
            'Created From','modifiedby Jhon Doe', '2038-01-19 03:14:07', 'Modifield From');
