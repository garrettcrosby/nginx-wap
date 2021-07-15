FROM nginx:alpine
#kill ipv6
RUN rm /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
RUN mkdir -p /etc/pki/certs/nginx
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY ./certs /etc/pki/certs/nginx/
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 443
STOPSIGNAL SIGQUIT
CMD ["nginx", "-g", "daemon off;"]

