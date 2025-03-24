output "alb_dns_name" {
  description = "DNS name of the Application Load Balancer"
  value       = aws_lb.ecs_alb.dns_name
}

output "ecs_cluster_name" {
  description = "ECS Cluster Name"
  value       = aws_ecs_cluster.my_cluster.name
}

output "ecs_service_name" {
  description = "ECS Service Name"
  value       = aws_ecs_service.nginx_service.name
}
