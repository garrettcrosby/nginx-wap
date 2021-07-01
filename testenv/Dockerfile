FROM nginx:alpine
RUN mkdir -p /etc/pki/certs/nginx
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY ./certs /etc/pki/certs/nginx/
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 443
STOPSIGNAL SIGQUIT
CMD ["nginx", "-g", "daemon off;"]

