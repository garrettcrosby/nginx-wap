FROM nginx:alpine
RUN rm /etc/nginx/nginx.conf
RUN mkdir -p /etc/pki/certs/nginx
COPY ./certs /etc/pki/certs/nginx/
COPY nginx.conf /etc/nginx/nginx.conf
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 443
STOPSIGNAL SIGQUIT
CMD ["nginx", "-g", "daemon off;"]

